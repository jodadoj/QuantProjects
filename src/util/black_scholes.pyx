# cython : language_level=3

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def black_scholes_cython_parallel2(int nopt,
                                   double[:] price,
                                   double[:] strike,
                                   double[:] t,
                                   double rate,
                                   double vol,
                                   bint ret_call=1):

    cdef double[:] ret = np.zeros(nopt, dtype=DTYPE)

    cdef int i

    cdef DTYPE_t d1, d2, n_d1, n_d2, s, p, e_rt, v, x, y

    with nogil, parallel():
        for i in prange(nopt, schedule='guided'):
            s = strike[i]
            p = price[i]
            v = vol * sqrt(t[i])
            x = log(p / s) + rate * t[i]
            y = vol * vol / 2. * t[i]

            d1 = (x + y) / v
            d2 = (x - y) / v

            n_d1 = 0.5 + 0.5 * erf(d1 / sqrt(2))
            n_d2 = 0.5 + 0.5 * erf(d2 / sqrt(2))

            e_rt = exp(-rate * t[i])

            if ret_call:
                ret[i] = p * n_d1 - e_rt * s * n_d2
            else:
                ret[i] = e_rt * s * -n_d2 - p * -n_d1

    return ret
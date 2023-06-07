"""Yield successive n-sized chunks from list"""


def chunks(chunk_list, no_of_chunks):
    """Yield successive n-sized chunks from list"""
    for i in range(0, len(chunk_list), no_of_chunks):
        yield chunk_list[i : i + no_of_chunks]

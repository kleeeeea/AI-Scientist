def main_():

    from dotenv import load_dotenv

    load_dotenv(dotenv_path=("/Users/l/.env"), override=True)

    import requests_cache
    from aider.coders import Coder
    from aider.io import InputOutput
    from aider.models import Model

    # Cache all requests for 1 hour
    requests_cache.install_cache("aider_cache", expire_after=3600)

    io = InputOutput()
    model = Model("gpt-4o-mini")  # or whatever model
    # First run hits the API
    create = Coder.create(main_model=model, io=io, stream=False, use_git=False, edit_format="diff", )
    out1 = create.run("explain caching in aider")

    # Second run within 1 hour comes from cache
    out2 = Coder.create(
            main_model=model,
            io=io,
            stream=False,
            use_git=False,
            edit_format="diff",
    ).run("explain caching in aider")

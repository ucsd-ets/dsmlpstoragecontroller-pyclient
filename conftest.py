from os import getenv

ADDRESS = getenv("ADDRESS")
PORT = getenv("PORT")
CA = getenv("CA")
CERT = getenv("CERT")
KEY = getenv("KEY")


# def pytest_addoption(parser):
#     parser.addoption(
#         "-address",
#         action="store",
#         help="Address for communicating with gRPC server",
#         default=ADDRESS,
#     )
#     parser.addoption(
#         "-port", action="store", help="Port for listening to gRPC server", default=PORT
#     )
#     parser.addoption(
#         "-ca",
#         action="store",
#         help="Path to server CA",
#         default=CA,
#     )
#     parser.addoption(
#         "-cert",
#         action="store",
#         help="Path to server certificate",
#         default=CERT,
#     )
#     parser.addoption(
#         "-key",
#         action="store",
#         help="Path to server key",
#         default=KEY,
#     )


# @pytest.fixture
# def addressopt(request):
#     return request.config.getoption("-address")


# @pytest.fixture
# def portopt(request):
#     return request.config.getoption("-port")


# @pytest.fixture
# def capathopt(request):
#     return request.config.getoption("-ca")


# @pytest.fixture
# def certpathopt(request):
#     return request.config.getoption("-cert")


# @pytest.fixture
# def keypathopt(request):
#     return request.config.getoption("-key")

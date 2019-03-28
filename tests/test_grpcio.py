from google.protobuf.json_format import MessageToDict, MessageToJson
from hamcrest import assert_that, equal_to, has_property

from grpc_helpers.grpc import call


class TestGrpc(object):

    def test_short_form(self, grpc_stuff):
        response_dict, response_details = call(grpc_stuff, 'SquareRoot', {'value': 16}, 'Number', timeout=1)
        correct_value = grpc_stuff[1].Number(value=4.0)
        assert_that(response_dict, equal_to(MessageToDict(correct_value)))
        assert_that(response_details.code().name, equal_to('OK'))

        response_json, _ = call(grpc_stuff, 'SquareRoot', {'value': 16}, 'Number', timeout=1, out='json')
        assert_that(response_json, equal_to(MessageToJson(correct_value)))

        response_raw, _ = call(grpc_stuff, 'SquareRoot', {'value': 16}, 'Number', timeout=1, out='raw')
        assert_that(response_raw, has_property('DESCRIPTOR'))

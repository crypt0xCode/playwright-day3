from ads_power.modules.base import Base


class Groups(Base):
    def new_group(self,
                  group_name: str | None = None,
                  remark: str | None = None):
        """
        Make new user group in ADS.
        :param group_name: Users group's name.
        :param remark: Group note.
        :return: Create group request.
        """
        path = '/api/v1/group/create'
        method = 'POST'
        params = {
            'group_name': group_name,
            'remark': remark,
        }

        return self.make_request(method=method,
                                 request_path=self.api_uri + path,
                                 params=params)


    def edit_group(self,
                   group_id: int,
                   group_name: str | None = None,
                   remark: str | None = None):
        """
        Edit group information.
        :param group_id: ID of group which must be edited.
        :param group_name: New users group's name.
        :param remark: Group note.
        :return: Edit group request.
        """
        path = '/api/v1/group/update'
        method = 'POST'
        params = {
            'group_id': group_id,
            'group_name': group_name,
            'remark': remark,
        }

        return self.make_request(method=method,
                                 request_path=self.api_uri + path,
                                 params=params)


    def query_group(
            self,
            group_name: str | None = None,
            page: str = '1',
            page_size: str = '1'
    ):
        path = '/api/v1/group/list'
        method = 'GET'
        params = {
            'group_name': group_name,
            'page': page,
            'page_size': page_size,
        }

        return self.make_request(
            method=method,
            request_path=self.api_uri + path,
            params=params
        )

    def get_group_id_by_group_name(self, group_name: str) -> str:
        groups_query = self.query_group(group_name=group_name)
        # {'data': {'list': [{'group_id': '5296878', 'group_name': 'test', 'remark': ''}], 'page': 1, 'page_size': 1}, 'code': 0, 'msg': 'Success'}
        try:
            group_id = groups_query.get('data').get('list')[0].get('group_id')
        except Exception as err:
            raise Exception(f'Can not get group id: {err}')
        return group_id


# ---------------------------------------------------------------------------------------
import config
import time
# Test methods.
# groups = Groups(api_key=config.ADS_API_KEY, api_uri=config.ADS_API_URI)
# print(groups.query_group(page_size='10'))
# time.sleep(3)
# groups.new_group('Second PW')
# time.sleep(1)
# ads_group_id = groups.get_group_id_by_group_name(group_name='ADS PW TEST4')
# time.sleep(1)
# ads_group2_id = groups.get_group_id_by_group_name(group_name='Second PW')
#
# print(ads_group_id)
# print(ads_group2_id)
# groups.edit_group(group_id=ads_group_id, group_name='ADS PW TEST4')
# time.sleep(3)
# print(groups.query_group())
# time.sleep(1)
# print(groups.query_group(group_name='test'))
# ---------------------------------------------------------------------------------------

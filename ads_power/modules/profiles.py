from ads_power.modules.base import Base
from ads_power.modules.groups import Groups
from ads_power.data.models import Proxy, Fingerprint


class Profiles(Base):
    def new_profile(
            self,
            group_name: str,
            proxy: Proxy,
            name: str | None = None,
            domain_name: str | None = None,
            open_urls: list[str] | None = None,
            repeat_config: list[str] | None = None,
            username: str | None = None,
            password: str | None = None,
            fakey: str | None = None,
            cookie: str | None = None,
            ignore_cookie_error: str = '0',
            ip: str | None = None,
            country: str | None = None,
            region: str | None = None,
            city: str | None = None,
            remark: str | None = None,
            ipchecker: str | None = None,
            sys_app_cate_id: str = '0',
            fingerprint_config: dict[str, str] | None = None
    ):
        path = '/api/v1/user/create'
        method = 'POST'
        params = {
            'group_id': Groups(self._api_key, self.api_uri).get_group_id_by_group_name(group_name),
            'user_proxy_config': proxy.get_dict(),
            'name': name,
            'domain_name': domain_name,
            'open_urls': open_urls,
            'repeat_config': repeat_config,
            'username': username,
            'password': password,
            'fakey': fakey,
            'cookie': cookie,
            'ignore_cookie_error': ignore_cookie_error,
            'ip': ip,
            'country': country,
            'region': region,
            'city': city,
            'remark': remark,
            'ipchecker': ipchecker,
            'sys_app_cate_id': sys_app_cate_id,
            'fingerprint_config': fingerprint_config
        }

        return self.make_request(
            method=method,
            request_path=self.api_uri + path,
            params=params
        )

    def update_profile_info(
            self,
            proxy: Proxy,
            proxy_id: str | None = None,
            user_id: str | None = None,
            name: str | None = None,
            domain_name: str | None = None,
            open_urls: list[str] | None = None,
            username: str | None = None,
            password: str | None = None,
            fakey: str | None = None,
            cookie: str | None = None,
            ignore_cookie_error: str = '0',
            ip: str | None = None,
            country: str | None = None,
            region: str | None = None,
            city: str | None = None,
            remark: str | None = None,
            sys_app_cate_id: str = '0',
            fingerprint_config: dict[str, str] | None = None
    ):
        path = '/api/v1/user/update'
        method = 'POST'
        params = {
            'user_id': user_id,
            'name': name,
            'domain_name': domain_name,
            'open_urls': open_urls,
            'username': username,
            'password': password,
            'fakey': fakey,
            'cookie': cookie,
            'ignore_cookie_error': ignore_cookie_error,
            'ip': ip,
            'country': country,
            'region': region,
            'city': city,
            'remark': remark,
            'sys_app_cate_id': sys_app_cate_id,
            'user_proxy_config': proxy.get_dict(),
            'proxy_id': proxy_id,
            'fingerprint_config': fingerprint_config
        }

        return self.make_request(
            method=method,
            request_path=self.api_uri + path,
            params=params
        )

    def query_profile(
            self,
            group_id: str | None = None,
            user_id: str | None = None,
            serial_number: str | None = None,
            user_sort: str | None = None,
            page: str | None = None,
            page_size: str | None = None
    ):
        path = '/api/v1/user/list'
        method = 'GET'
        params = {
            'group_id': group_id,
            'user_id': user_id,
            'serial_number': serial_number,
            'user_sort': user_sort,
            'page': page,
            'page_size': page_size
        }

        return self.make_request(
            method=method,
            request_path=self.api_uri + path,
            params=params
        )

    def delete_profile(
            self,
            user_ids: []
    ):
        path = '/api/v1/user/delete'
        method = 'POST'
        params = {
            'user_ids': user_ids
        }

        return self.make_request(
            method=method,
            request_path=self.api_uri + path,
            params=params
        )

    def move_profile(
            self,
            user_ids: [],
            group_id: str | None = None
    ):
        path = '/api/v1/user/regroup'
        method = 'POST'
        params = {
            'user_ids': user_ids,
            'group_id': group_id
        }

        return self.make_request(
            method=method,
            request_path=self.api_uri + path,
            params=params
        )

    def delete_cache(self):
        return self.make_request(
            method='POST',
            request_path=self.api_uri + '/api/v1/user/delete-cache',
            params={}
        )


# ---------------------------------------------------------------------------------------
import config
import time


proxy = Proxy()
proxy = Proxy(proxy_line='http://ip:port@login:password')
profiles = Profiles(api_key=config.ADS_API_KEY, api_uri=config.ADS_API_URI)

# Test methods.
# print(profiles.new_profile(group_name='ADS PW TEST', proxy=proxy))
# time.sleep(1)
# print(profiles.new_profile(group_name='ADS PW TEST', proxy=proxy, name='test_20'))
# time.sleep(1)
# print(profiles.new_profile(group_name='ADS PW TEST', proxy=proxy, name='test_3', fingerprint_config=Fingerprint.get_config()))
# print(profiles.query_profile(group_id='5744827', page_size='5'))
# time.sleep(1)
# profiles.delete_profile(user_ids=['ktndw19'])
# time.sleep(1)
# print(profiles.query_profile(group_id='5745208', page_size='5'))
# profiles.move_profile(user_ids=['ktndw09'], group_id='5745208')
#
# print(profiles.query_profile(group_id='5744827', page_size='5'))
# time.sleep(1)
# print(profiles.query_profile(group_id='5745208', page_size='5'))
# time.sleep(1)
# profiles.update_profile_info(proxy=proxy, user_id='ktndvy3', username='test-pw-now')
# time.sleep(1)
# print(profiles.query_profile(group_id='5744827', page_size='5'))
# ---------------------------------------------------------------------------------------

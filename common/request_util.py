# @Time : 2025/2/11 16:19
# @Author : luoxin
import logging

import requests


class RequestUtil:
    def __init__(self, headers=None,auth=None):
        self.headers = headers or {}
        self.auth = auth
        self.session = requests.session()

    def send_request(self, method, url,params=None, data=None, json=None):
        try:
            logging.info(f"Sending {method} request to {url} with params {params} or data {data} or json {json}")

            if method.upper() == "GET":
                response = self.session.get(url, headers=self.headers, params=params,auth=self.auth)
            elif method.upper() == "POST":
                response = self.session.post(url, headers=self.headers, data=data,json=json,auth=self.auth)
            elif method.upper() == "PUT":
                response = self.session.put(url, headers=self.headers, data=data,json=json,auth=self.auth)
            elif method.upper() == "DELETE":
                response = self.session.delete(url, headers=self.headers, params=params,auth=self.auth)
            else:
                raise ValueError(f"Unsupported method: {method}")

            logging.info(f"Received responses: {response.status_code}")
            logging.debug(f"Response body: {response.text}")

            # 自动检查 4xx/5xx 错误，如有异常则抛出
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP error occurred: {e}")
            raise
        except Exception as e:
            logging.error(f"Unknown error occurred: {e}")
            raise

    def close(self):
        """关闭会话"""
        logging.info("Closing session")
        self.session.close()

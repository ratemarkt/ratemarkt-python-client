import os
import requests


class RatemarktClientError(Exception):

    def __init__(self, error_obj):
        super(RatemarktClientError, self).__init__(error_obj.get('message'))
        self.error_obj = error_obj


class RatemarktClient:

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def _request(self, path, query):
        print query
        url = os.path.join(self.base_url, path)
        headers = {'Authorization': 'Bearer %s' % self.api_key}
        response = requests.post(url, json=query, headers=headers)
        if response.ok:
            return response.json()
        else:
            error_obj = None
            try:
                error_obj = response.json()
            except:
                pass
            if error_obj:
                print error_obj
                raise RatemarktClientError(error_obj)
            else:
                raise Exception(response.text)

    def populate_paxes(self, pax_list):
        paxes = []
        for pax in pax_list:
            paxes.append({
                'numberOfAdults': pax[0],
                'childrenAges': pax[1:] if len(pax) > 1 else []
            })
        return paxes

    def check_hotels(self, destination_code, hotel_code_list, checkin,
                     checkout, pax_list, currency, nationality):
        query = {
            'destinationCode': destination_code,
            'hotelCodes': hotel_code_list,
            'checkin': checkin.strftime('%Y-%m-%d'),
            'checkout': checkout.strftime('%Y-%m-%d'),
            'paxes': self.populate_paxes(pax_list),
            'currency': currency,
            'nationality': nationality
        }
        return self._request('checkhotels', query)

    def check_hotel(self, hotel_code, checkin, checkout, pax_list, currency,
                    nationality):
        query = {
            'hotelCode': hotel_code,
            'checkin': checkin.strftime('%Y-%m-%d'),
            'checkout': checkout.strftime('%Y-%m-%d'),
            'paxes': self.populate_paxes(pax_list),
            'currency': currency,
            'nationality': nationality
        }
        return self._request('checkhotel', query)

    def check_rate(self, rate_key):
        query = {
            'rateKey': rate_key,
        }
        return self._request('checkrate', query)

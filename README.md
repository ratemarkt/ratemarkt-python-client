# Ratemarkt Python Client

Python client library for Ratemarkt API

## Usage

```python
>>> from datetime import date
>>> from ratemarkt import RatemarktClient

>>> c = RatemarktClient('RATEMARKT_API_URL', 'YOU_API_KEY')
>>> c.check_hotels('928b37', None, date(2017, 06, 22), date(2017, 06, 25), [(2,)],
               'USD', 'US')

{u'debugData': None,
 u'hotels': [{u'countryCode': u'us',
   u'destinationCode': u'928b37',
   u'destinationName': u'istanbul',
   u'hotelCode': u'0aef99',
   u'hotelName': u'The Marmara Pera',
   u'rates': [{u'boardName': u'Room Only',
     u'cancellationPolicies': [{u'amount': 69.0,
       u'fromDate': u'2017-06-22T12:00:00Z'},
      {u'amount': 0.0, u'fromDate': u'2017-06-21T12:00:00Z'}],
     u'commission': 10.35,
     u'currency': u'EUR',
     u'hotelCurrency': u'USD',
     u'hotelRate': 243.93,
     u'nonrefundable': False,
     u'rate': 250.39,
     u'rateKey': u'[Q7s|3|USD|US|[[2|[]]]]_[dMSP|Cu-Z|DIRECT|0|NWv9zw|[fvIDCw|2|0]]',
     u'rateType': u'DIRECT',
     u'remarks': None,
     u'rooms': [{u'numberOfAdults': 2,
       u'numberOfChildren': 0,
       u'roomDescription': u'Superior Room, City View',
       u'sequence': 1}]},
    {u'boardName': u'Room Only',
     u'cancellationPolicies': [{u'amount': 227.58,
       u'fromDate': u'2017-06-22T12:00:00Z'},
      {u'amount': 227.58, u'fromDate': u'2017-05-11T21:00:00Z'}],

...
```
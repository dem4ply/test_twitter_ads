from unittest.mock import MagicMock

all_account = MagicMock( status_code=200 )
all_account.json.return_value = {
	"request": {
		"params": {
		}
	},
	"data": [
		{
			"name": "Sandbox account for @AdsAPI",
			"timezone": "America/Los_Angeles",
			"timezone_switch_at": None,
			"id": "xxxxxx",
			"created_at": "2014-03-09T00:41:49Z",
			"salt": "f9f9d5a5f23075c618da5eb1d1a9df57",
			"updated_at": "2015-01-29T00:41:49Z",
			"approval_status": "ACCEPTED",
			"deleted": False
		}
	],
	"data_type": "account",
	"total_count": 1,
	"next_cursor": None 
}

one_account = MagicMock( status_code=200 )
one_account.json.return_value = {
	"data": {
		"approval_status": "ACCEPTED",
		"created_at": "2014-07-14T22:51:48Z",
		"deleted": False,
		"id": "hkkd",
		"name": "Some person named Emma",
		"salt": "973fef8gce1c5d5f6bba4b91827c214a",
		"timezone": "America/Los_Angeles",
		"timezone_switch_at": "2014-07-27T07:00:00Z",
		"updated_at": "2014-08-27T21:59:56Z"
	},
	"data_type": "account",
	"request": {
		"params": {
				"account_id": "hkkd"
		}
	}
}

all_instruments = MagicMock( status_code=200 )
all_instruments.json.return_value = {
	"data": [
		{
			"account_id": "xxxxxx",
			"cancelled": True,
			"created_at": "2014-03-09T00:41:49Z",
			"credit_limit_local_micro": None,
			"currency": "USD",
			"deleted": False,
			"description": None,
			"end_time": None,
			"funded_amount_local_micro": None,
			"id": "yyyy",
			"start_time": "2014-05-29T00:41:49Z",
			"type": "CREDIT_CARD",
			"updated_at": "2014-05-29T00:41:49Z"
		}
	],
	"data_type": "funding_instrument",
	"next_cursor": None,
	"request": {
		"params": {
			"account_id": "xxxxxx"
		}
	},
	"total_count": 1
}

one_instrument = MagicMock( status_code=200 )
one_instrument.json.return_value = {
	"data": {
		"account_id": "hkk5",
		"cancelled": False,
		"created_at": "2012-11-08T02:31:46Z",
		"credit_limit_local_micro": 1000000000,
		"currency": "USD",
		"deleted": False,
		"description": "MasterCard ending in 1234",
		"end_time": None,
		"funded_amount_local_micro": 100000000,
		"id": "hw6ie",
		"start_time": "2012-11-08T02:31:46Z",
		"type": "CREDIT_CARD",
		"updated_at": "2012-11-20T23:20:35Z"
	},
	"data_type": "funding_instrument",
	"request": {
		"params": {
			"account_id": "hkk5",
			"funding_instrument_id": "hw6ie"
		}
	}
}

all_campaigns = MagicMock( status_code=200 )
all_campaigns.json.return_value = {
	"data": [
		{
			"name": "KEEP TWITTER WEIRD",
			"created_at": "2012-11-20T23:29:09Z",
			"end_time": None,
			"updated_at": "2012-11-30T23:06:46Z",
			"account_id": "hkk5",
			"deleted": False,
			"id": "7jem",
			"paused": True,
			"total_budget_amount_local_micro": 72000000,
			"currency": "USD",
			"daily_budget_amount_local_micro": 18000000,
			"funding_instrument_id": "hw6ie",
			"start_time": "2012-11-20T23:30:00Z",
			"standard_delivery": True
		},
		{
			"name": "Follow @twitterapi",
			"end_time": None,
			"created_at": "2012-11-30T22:58:11Z",
			"updated_at": "2012-12-02T05:10:52Z",
			"account_id": "hkk5",
			"id": "7wdy",
			"deleted": False,
			"paused": True,
			"total_budget_amount_local_micro": 20000000,
			"currency": "USD",
			"daily_budget_amount_local_micro": 10000000,
			"funding_instrument_id": "hw6ie",
			"start_time": "2012-11-30T22:56:00Z",
			"standard_delivery": True
		}
	],
	"data_type": "campaign",
	"request": {
		"params": {
			"with_deleted": True,
			"account_id": "hkk5"
		}
	},
	"total_count": 2
}

one_campaigns = MagicMock( status_code=200 )
one_campaigns.json.return_value = {
	"data": {
		"account_id": "xxxxxx",
		"created_at": "2015-02-09T00:00:00Z",
		"currency": "USD",
		"daily_budget_amount_local_micro": 50000000,
		"deleted": False,
		"end_time": None,
		"funding_instrument_id": "yyyy",
		"id": "92ph",
		"name": "My First Campaign",
		"paused": False,
		"standard_delivery": True,
		"start_time": "2015-02-09T00:00:00Z",
		"total_budget_amount_local_micro": 500000000,
		"updated_at": "2015-02-09T00:00:00Z"
	},
	"data_type": "campaign",
	"request": {
		"params": {
			"campaign_id": "7jem",
			"account_id": "hkk5"
		}
	}
}


one_line = MagicMock( status_code=200 )
one_line.json.return_value = {
	"data_type": "line_item",
	"data": {
		"bid_type": "MAX",
		"name": "Untitled",
		"placements": [
			"ALL_ON_TWITTER"
		],
		"bid_amount_local_micro": 1500000,
		"automatically_select_bid": False,
		"advertiser_domain": None,
		"primary_web_event_tag": None,
		"charge_by": "ENGAGEMENT",
		"product_type": "PROMOTED_TWEETS",
		"bid_unit": "ENGAGEMENT",
		"total_budget_amount_local_micro": None,
		"objective": "TWEET_ENGAGEMENTS",
		"id": "azjx",
		"paused": True,
		"account_id": "xxxxxxx",
		"optimization": "DEFAULT",
		"categories": [],
		"currency": "USD",
		"created_at": "2015-02-09T00:00:00Z",
		"updated_at": "2015-02-09T00:00:00Z",
		"include_sentiment": "POSITIVE_ONLY",
		"campaign_id": "92ph",
		"deleted": False
	},
	"request": {
		"params": {
			"placements": [
				"ALL_ON_TWITTER"
			],
			"bid_amount_local_micro": 1500000,
			"product_type": "PROMOTED_TWEETS",
			"paused": True,
			"account_id": "xxxxxxx",
			"campaign_id": "92ph"
		}
	}
}

all_target = MagicMock( status_code=200 )
all_target.json.return_value = {
	"data": [
		{
			"name": "San Francisco-Oakland-San Jose CA, US",
			"targeting_type": "LOCATION",
			"targeting_value": "5122804691e5fecc"
		}
	],
	"data_type": "targeting_criterion",
	"request": {
		"params": {
			"location_type": "CITY",
			"q": "San Francisco"
		}
	}
}

one_target = MagicMock( status_code=200 )
one_target.json.return_value = {
	"data": {
		"account_id": "xxxxxx",
		"created_at": "2015-02-09T00:00:15Z",
		"deleted": False,
		"id": "2u3be",
		"line_item_id": "yyyy",
		"name": "San Francisco-Oakland-San Jose CA, US",
		"targeting_type": "LOCATION",
		"targeting_value": "5122804691e5fecc",
		"updated_at": "2013-05-30T21:01:35Z"
	},
	"data_type": "targeting_criterion",
	"request": {
		"params": {
			"account_id": "xxxxxx",
			"line_item_id": "yyyy",
			"targeting_type": "LOCATION",
			"targeting_value": "5122804691e5fecc"
		}
	}
}

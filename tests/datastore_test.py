import datetime
from unittest import mock

from google.cloud import datastore
from data_sources.datastore import DataStore


# Mock_datastore, questionnaire, live_date come from conftest.py
def test_add_livedate_with_valid_fields(mock_datastore, questionnaire, live_date):
    mocked_key = mock.MagicMock(name=questionnaire.upper())
    mock_datastore.key.return_value = mocked_key
    data_source = DataStore(client=mock_datastore, project_id="foo")
    mock_entity = datastore.Entity(key=mocked_key)
    mock_entity["questionnaire"] = questionnaire.upper()
    mock_entity["livedate"] = live_date

    assert data_source.add_livedate(questionnaire, live_date) == {questionnaire.upper(): live_date.isoformat()}
    mock_datastore.key.assert_called_once_with("LiveDate", questionnaire.upper())
    mock_datastore.put.assert_called_once_with(mock_entity)


def test_get_livedate(mock_datastore, questionnaire):
    print("hello")
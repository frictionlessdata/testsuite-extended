Feature: Datapackage integrations

  Scenario Outline: Push/pull datapackage to storage
    When We push/pull datapackage from "<dataset>" to <backend>
    Then No errors are occured

    Examples: BigQuery
        | backend  | dataset                      |
        | BigQuery | country-list                 |
        | BigQuery | nasdaq-listings              |
        | BigQuery | synthetic                    |

    Examples: SQL
        | backend  | dataset                      |
        | SQL      | country-list                 |
        | SQL      | gb-country-regional-analysis |
        | SQL      | nasdaq-listings              |
        | SQL      | registry                     |
        | SQL      | synthetic                    |

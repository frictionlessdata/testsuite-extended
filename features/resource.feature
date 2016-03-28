Feature: Resource operations

  # BigQuery

  Scenario Outline: Push/pull resource to BigQuery storage
    When We push/pull resource from "<dataset>" to BigQuery
    Then No errors are occured

    Examples: Datasets
        | dataset |
        | testing |

  # SQL

  Scenario Outline: Push/pull resource to SQL storage
    When We push/pull resource from "<dataset>" to SQL
    Then No errors are occured

    Examples: Datasets
        | dataset |
        | testing |

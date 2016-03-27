Feature: JSON Table Schema core and integrations work

  Scenario Outline: Push/pull resource to SQL storage
    When We push/pull resource from "<path>" to SQL
    Then No errors are occured

    Examples: Synthetic
        | path                       |
        | datasets/resources/testing |

  Scenario Outline: Push/pull resource to BigQuery storage
    When We push/pull resource from "<path>" to BigQuery
    Then No errors are occured

    Examples: Synthetic
        | path                       |
        | datasets/resources/testing |

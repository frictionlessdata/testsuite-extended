Feature: JSON Table Schema works with SQL storage

  Scenario Outline: Push/pull to SQL storage
    When We push/pull resource from "<path>" to SQL
    Then No errors are occured

    Examples: Synthetic
        | path                       |
        | datasets/resources/testing |

Feature: JSON Table Schema works with SQL storage

  Scenario Outline: Push/pull to storage: <path>
    When We push/pull resource from "<path>" to sql
    Then No errors are occured

    Examples: Synthetic
        | path                       |
        | datasets/resources/testing |

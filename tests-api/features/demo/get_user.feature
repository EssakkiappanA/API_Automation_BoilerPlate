@Regression @sample
Feature: Navigation
    Navigation to ComplicatedPage

    @automated @get-method
    Scenario Outline: Gets  user without authentication
        Given I am using <auth_type>
        When I call for <verb> <endpoint> <queryparam> <body>
        Then I get <response_code>
        Then I validate <value> in <path>
        Examples:
            | auth_type | verb | endpoint     | queryparam | response_code | value             | path                | body      |
            |           | GET  | /api/users/2 |            |    200        | Janet             | 'data'.'first_name' |           |
            |           | GET  | /api/users/2 |            |    200        | Weaver            | 'data'.'last_name'  |           |
            |           | GET  | /api/unknown |            |    200        | cerulean          | 'data'[0].'name'    |           |
            |           | GET  | /api/users   | page=2     |    200        | 7                 | 'data'[0].'id'      |           |
            |           | GET  | /api/users/23|            |    404        |                   |                     |           |
            |           | POST | /api/users   |            |    201        | hello          | 'name'              | user_data |
            |           | POST | /api/register|            |    200        | QpwL5tke4Pnpja7X4 | 'token'             | reg_success |



@terllo_demo
Feature: Trello Board Creation API demo
    Validating various api on terllo application

    @automated @trello
    Scenario Outline: Gets  user without authentication
       Given I am using <auth_type>
       When I call for <verb> <endpoint> <queryparam>
       Then I get <response_code>
       Then I validate <value> in <path>
       Examples:
           | auth_type | verb | endpoint     | queryparam | response_code | value    | path                |
           | OAUTH2    | GET  | /api/users/2 |            |    200        | Janet    | 'data'.'first_name' |
           | OAUTH2    | GET  | /api/users/2 |            |    200        | Weaver   | 'data'.'last_name'  |
           | OAUTH2    | GET  | /api/unknown |            |    200        | cerulean | 'data'[0].'name'    |
           | OAUTH2    | GET  | /api/users   | page=2     |    200        | 7        | 'data'[0].'id'      |

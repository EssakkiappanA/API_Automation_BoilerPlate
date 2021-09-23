@ID-of-Epic
Feature: Navigation
    Navigation to ComplicatedPage

    @automated
    Scenario Outline: Gets user
        Given I am using <auth_type>
        When I call for <verb> <endpoint>
        # Then I get <response_code> and <response_message>
        Then I get <response_code>
        Then I validate <value> in <path>
        Examples:
            | auth_type | verb | endpoint | response_code | value | path |
            |           | GET  | /api/users/2 | 200 | Janet | 'data'.'first_name' |
            |           | GET  | /api/users/2 | 200 | Weaver | 'data'.'last_name' |
            |           | GET  | /api/unknown | 200 | cerulean | 'data'[0].'name' |



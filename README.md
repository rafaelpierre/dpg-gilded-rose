# Gilded Rose Kata

## Refactoring Exercise

### Overview

#### Implementation Approach

* By reading the requirements document, we understand that there are main/vanilla use cases (general business rules which apply to *all types of items*), as well as some specific ones (*e.g. Aged Brie, Backstage Passes*).
* We start the implementation by writing *failing test cases* for the main use cases, followed by their implementation.
* Once general test cases are working, we proceed by writing *failing test cases* for more specific items. Implementation of classes containing the required functionality follows accordingly.

#### StandardItem Class

* Some product behaviors are shared by all types of products, while other products display unique behavior in terms of business rules. For this reason, I opted for a design where there is a main class implementing the default behaviors (*StandardItem* class). This class is then inherited by other classes.
  * *StandardItem* inherits from the existing *Item* class. This choice was made purely due to the *fictitious* constraint which prevents us from making changes to this class. Hence we leverage the existing *Item* implementation and complement it with the logic added to the *StandardItem* class.
  * **Observation:** in a real world scenario, best approach would be to re-write the Item class.

#### "Specific Behavior" Classes

* There are products which adhere to the business rules from *StandardItem* but also display specific behavior.
For these cases, I decided to implement specific classes (e.g. *AgedBrie*, *BackstagePass*). These classes inherit from *StandardItem*.

#### Comments

The exercise requires refactoring, but also the implementation of new functionality:

* *"Conjured" items degrade in Quality twice as fast as normal items*

* There are three main sources which served as guides in this refactoring exercise:
  * The requirements document;
  * The existing test fixtures;
  * The existing logic;
  * Unit testing & test coverage

* Although detailed, the requirements can be a bit ambiguous sometimes. This requires some opinionated choices when it comes to implementation

### Implementation Details

#### ItemFactory and ItemType

* **ItemFactory** implements the **Simple Factory** pattern. It contains a static *create_item* method which generates objects of the correct class, based on the *name* parameter.
* This approach was used to keep compatibility with the way parameters are passed in the existing implementation/fixtures in a clean, simple way.
* **ItemType** is an Enum containing possible different item types. It was created to make the instantiation of classes cleaner and simpler.

### Testing

* Following TDD best practices, implementation was done in an iterative process. Failing tests were written followed by implementation of the required logic.
* Additionally, results from *texttest_fixture.py* were generated for both **legacy** (**legacy** branch) and **updated** (**main** branch) versions, and compared. This was done to confirm that previous logic was preserved.
  * It is noticed that the logic *Conjured* items was broken/not implemented in the legacy version (quality decreases by one, as opposed to requirements)
* Minimum code coverage of 100% was set as a project parameter within Poetry


#### Environment Settings & Details

* This project relies on (Poetry)[https://poetry.com] for dependency and environment management.
* Once Poetry is setup and dependencies are properly installed, one can run:
  * ```make test``` for testing
  * ```make coverage``` for generating test coverage report
  * ```make lint``` for linting with **flake8**
  * ```make black-fix``` for formatting with **black**
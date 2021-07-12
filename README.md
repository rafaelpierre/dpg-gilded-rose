# Gilded Rose Kata

## Refactoring Exercise

### Overview

The exercise requires refactoring, but also the implementation of new functionality:

* *"Conjured" items degrade in Quality twice as fast as normal items*

* There are three main sources which served as guides in this refactoring exercise:
  * The requirements document;
  * The existing test fixtures;
  * The existing logic;
  * Unit testing & test coverage

* Although detailed, the requirements can be a bit ambiguous sometimes. This requires some opinionated choices when it comes to implementation

#### Implementation Approach

* By reading the requirements document, we understand that there are main/vanilla use cases (general business rules which apply to *all types of items*), as well as some specific ones (*e.g. Aged Brie, Backstage Passes*).
* We start the implementation by writing *failing test cases* for the main use cases, followed by their implementation.
* Once general test cases are working, we proceed by writing *failing test cases* for more specific items. Implementation of classes containing the required functionality follows accordingly.

##### StandardItem Class

* Some product behaviors are shared by all types of products, while other products display unique behavior in terms of business rules. For this reason, I opted for a design where there is a main class implementing the default behaviors (*StandardItem* class). This class is then inherited by other classes.
  * *StandardItem* inherits from the existing *Item* class. This choice was made purely due to the constraint related to making changes in this class. Hence we leverage the existing *Item* implementation and complement it with the logic added to the *StandardItem* class.
  * **Observation:** in a real world scenario, best approach would be to re-write the Item class.

##### "Specific Behavior" Classes

* There are products which adhere to the business rules from *StandardItem* but also display specific behavior.
For these cases, I decided to implement specific classes (e.g. *AgedBrie*, *BackstagePass*). These classes inherit from *StandardItem*.

#### ItemFactory and ItemType

* **ItemFactory** class contains a basic, static *create_item* method which generates objects of the correct class, based on the *name* parameter.
* This approach was used to keep compatibility with the way parameters are passed in the existing implementation in a clean and simple way.
* **ItemType** is an Enum containing possible different item types.

#### Testing

* Following TDD best practices, implementation was done in an iterative process
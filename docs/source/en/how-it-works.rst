How It Works
==========================

Amadla CLI is the utility application to render templates based on grouped configuration files (YAML) following schemas
(https://json-schema.org/) to validate and document each property in the entity confiuration file.

Why are configuration files called entity?
-------------------------------------------

Simply because it is a very general term. An entity could be anything. In closes thing it ressembles in computer programming
would be a function/method. But since Amadla entities are closer related to configuration files, calling the grouping a
function or a method would cause more confusion than anything.

It seems similar to Docker compose
-------------------------------------------

It is. The Amadla project is trying to avoid reinventing the wheel as much as possible. This is why the need for Git is
required for entity management, for schema JSON-schema.org is used and the popular Jinja2 template engine is used.

The same goes for the naming conventions and specifications of the properties in the entities.

What is the difference between an Amadla entity and a Docker compose?
--------------------------------------------

1. Scope: Docker compose is for containers only and a Amadla entity could be for an application, a KVM virtual machine, a group of servers, anything.
2. Amadla entity configurations are merged together and like CSS they are put together in a cascading way. So this way default values for an entity can be set but overwritten by a child entity.
3. Amadla entity also comes with functionalities that we often find in other programming languages.

What are the differences with Docker compose?
---------------------------------------------

Outside of the limited procedural functionalities, it also comes with configuration properties that are not found in Docker compose.
For example: require, optional, supported and entity.

* entity: defines what is the parent entity. It defines what are the schemas to use and templates to render. Again all can be overwriten.
* optional: defines what entities are optionals for the itself.
* require: defines what entities are required for itself.
* supported: is a property found in a none-defining entity (e.g: a a DB entity that list what DB the main entity supports)

Entity scope
------------------

Entities have their own schemas but depending how they are implemented they change scope. This is more about definitions
than anything else. It does not have any impact on behavior or rendering of configuration files.

* parent entity:
* definition entity:
* setting entity:

Rendering of templates
-------------------------

https://github.com/compose-spec/compose-spec/blob/master/spec.md
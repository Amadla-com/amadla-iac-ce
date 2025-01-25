How It Works
==========================

Before diving in the details of functionality and behavior lets define the elements that are used by Amadla.

There are three types of files in Amadla:

* Entity YAML configuration file (`amadla.yml` found at the root of the repository)
* Schema, that defines the structure, the value types and documents the configuration components. Used for validation and documentation.
* Templates that are in Jinja2 format (`.j2`)

File types
--------------

Entity
~~~~~~~~

Entity files are in the YAML format.

Very similar to Podman compose files they define the requirements or optional elements that are needed for an entity.
It could be network settings like port numbers or a DB requirement.

```yaml

```

Schema
~~~~~~~~~~~

To make sure that a entity configuration file does not turn into dumpster fire it is useful to define the specs for the configuration elements.
The schemas use the (https://json-schema.org/) format to define the specs of an entity. This format also supports properties like description
that are useful for documentation the parts of the configuration standard that is defined.

Template
~~~~~~~~~~~~~

Templates are for generating configuration files. Using the popular Python template engine Jinja2.

Flow
-------------

[create the .amadla directory if if does not exist] ->
[Download entities repository with Git] ->
[]

FAQ
======

Amadla CLI is the utility application to render templates based on grouped configuration files (YAML) following schemas
(https://json-schema.org/) to validate and document each property in the entity confiuration file.

Why Python?
---------------

It could of easily been programmed with Golang or some other programming.

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
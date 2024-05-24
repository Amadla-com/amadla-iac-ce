Dev
=========================

There are many layers of automation in Amadla. This makes it very easy
to make a small mistakes that can have a cascading affect on all the
other layers of automation for this reason it is important for anyone
who wants to contribute to familiarize themselves with this
documentation.

Rules
------------------------

1. `Fail-fast! <https://en.wikipedia.org/wiki/Fail-fast>`__ - No, it is
   a not a new Fast & Furious movie. It is all about clear errors and
   avoiding cascading issues that make it very hard to clean up and
   debug a problem.

   -  Don’t hesitate to put conditions to verify if a value is valid.
   -  Catch as many possible failures.
   -  Testing the fails is a way to make sure we follow the fail-fast
      principle as much as possible.

2. Every time you make a change to one of the different ways to run
   Amadla you need to make sure it is mirrored to all the other ways
   (`Jenkins <../Jenkinsfile>`__, `GitHub
   Workflow <../.github/workflows/generate.yml>`__ –NOTE– Maybe Worflow
   can just call Jenkin script instead of having a whole seperated CI/CD
   –NOTE–, `containers <../containers/Makefile>`__ ???, or all the
   `tools installed on the system itself <../Makefile>`__).
3. Documentation is crucial! Also it is helpful to add links to the
   terms, accronyms, or concepts that might not be well known to the
   average person. Let make it easy.
4. Testing.

   -  With the four different ways to run Amadla.
   -  As many cloud environment as possible
   -  Basics:

      -  `AWS <https://aws.amazon.com/>`__
      -  `Azure <https://azure.microsoft.com/>`__
      -  `Google Cloud <https://cloud.google.com/>`__
      -  `DigitalOcean <https://www.digitalocean.com/>`__
      -  `Linode <https://www.linode.com/>`__
      -  `Vultr <https://www.vultr.com/>`__
      -  `RackSpace <https://www.rackspace.com/>`__ (or any other cloud
         services that uses `OpenStack <https://www.openstack.org/>`__))
      -  `CloudStack <https://cloudstack.apache.org/>`__\ (??? - unsure)

   -  Testing the other layers of automation.

5. Following the rules of:

   -  ```.editorconfig`` <../.editorconfig>`__
   -  ```.gitattributes`` <../.gitattributes>`__.

:information_source: Resources
------------------------------

-  `Demystifying Ansible Automation Controller \|
   GitHub <https://github.com/jnbdz/Demystifying-Ansible-Automation-Controller>`__
-  `Full Stack AWS Application Development \|
   GitHub <https://github.com/jnbdz/Full-Stack-AWS-Application-Development>`__
-  `Cloud Native Observability \|
   GitHub <https://github.com/jnbdz/Cloud-Native-Observability>`__
-  `Go for DevOps \| GitHub <https://github.com/jnbdz/Go-for-DevOps>`__
-  `Ansible for Real life Automation \|
   GitHub <https://github.com/jnbdz/Ansible-for-Real-life-Automation>`__
-  `HashiCorp Packer in Production \|
   GitHub <https://github.com/jnbdz/HashiCorp-Packer-in-Production>`__

Makefile
--------

Rules: - Uppercase is for global variables and lowercase is for a
specific target

   Might remove!

:package: Containers
--------------------

:cook: Compose
~~~~~~~~~~~~~~

:military_helmet: Manage Secrets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Many applications and services need secrets like username, password, TLS
keys, SSH keys, etc.

Since Amadla uses compose, here is an example of a compose configuration
that uses secrets:

.. code:: yaml

     secrets:
       nextcloud_admin_password:
       nextcloud_admin_user:
       postgres_db:
       postgres_password:
       postgres_user:

This example is taken from NextCloud.

Podman and Docker have tools to manage secrets.

.. code:: bash

   podman secret --help

Results:

::

   Manage secrets

   Description:
     Manage secrets

   Usage:
     podman secret [command]

   Available Commands:
     create      Create a new secret
     inspect     Inspect a secret
     ls          List secrets
     rm          Remove one or more secrets

:luggage: Module
----------------

Modules are found in ``apps.d``, ``servers.d`` and ``clouds.d``.

:left_luggage: Adding a Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most of Amadla is tightly integrated with Git with the usage of branches
and tags. It is not tightly attached to GitHub so you can easily use
another Git server. But using another code versioning system would be
very difficult.

The structure needs to follow the standard so that Amadla is able to use
and integrate the module.

:shinto_shrine: Jinja
~~~~~~~~~~~~~~~~~~~~~

Documentation: https://jinja.palletsprojects.com/en/3.1.x/templates/

:ocean: Git flow
~~~~~~~~~~~~~~~~

Amadla is tightly

Ini:

.. code:: bash

   git flow init

..

   For ``Version tag prefix? [] v``

Start a new feature:

.. code:: bash

   git flow feature start pilot

It will return:

.. code:: bash

   git flow feature start pilot
   Switched to a new branch 'feature/pilot'

   Summary of actions:
   - A new branch 'feature/pilot' was created, based on 'develop'
   - You are now on branch 'feature/pilot'

   Now, start committing on your feature. When done, use:

        git flow feature finish pilot

Git push the new branch:

.. code:: bash

   git push --set-upstream origin feature/pilot

:gem: Applications
^^^^^^^^^^^^^^^^^^

Here is the list of the essentials for **applications**: - ``config/`` -
The ``config`` directory contains the configurations, most of it is
Jinja format. - ``compose.yml.j2`` - This is the Jinja template for the
container compose file that is used by the container engine (Podman or
Docker). If the application is installed - ``docs/`` (optional) - The
``docs`` directory contains the Markdown documentation. Only needed if
there are special actions, details, development instructions. -
``LICENSE`` - ``module.yml`` - - ``README.md`` -

:paperclips: ``config/``
''''''''''''''''''''''''

:paperclip: ``compose.yml.j2``
''''''''''''''''''''''''''''''

:baggage_claim: ``module.yml``
''''''''''''''''''''''''''''''

Lets start with an example:

.. code:: yaml

   ---
   version: 1
   module:
     description: Vault - Secret tool.
     authors:
       - Jean-Nicolas Boulay (JN) <https://jean-nicolas.name>
     category: Application
     tags:
       - keys
       - security
       - password
       - secrets
       - storage
     configuration:
       network:
         internal:
           ports:
             - protocol: tcp
               internal: 8080
               external: 8080
         private:
           locations:
             - location: /vault
               ports:
                 - protocol: tcp
                   internal: 8200
                   external:

-  ``version`` - Is the first key to indicate the version of the
   ``module.yml`` configuration file.
-  ``module`` - Is to groupe all the module settings.
-  ``description`` - The description of the module and what it is about.
-  ``authors`` (optional) - You can list the authors of the module.
-  ``type`` - …
-  ``category`` - There are three categories you can use:

   -  Application
   -  Server
   -  Cloud

-  ``tags`` - Is a list of words that help grouping modules.
-  ``configuration`` -

   -  ``network`` -

      -  :red_circle: ``protected`` - This means that only services and
         applications can be access internaly in the same server.
      -  :yellow_circle: ``internal`` - This indicates to Amadla that
         this can only be access by internal services and applications.

         -  ``locations`` - List of locations (in case you need multiple
            paths).
         -  ``ports`` - List of ports and protocols that are used with
            the entrypoint, firewall and container.

            -  ``protocol`` (optional) - ``tcp`` or ``udp`` (default
               ``tcp``).
            -  ``internal`` - This is the port **in** the container
               (example: **8080**:80).
            -  ``external`` - This is the port **outside** of the
               container (example: 8080:**80**).

      -  :large_blue_circle: ``private`` - This indicates to Amadla that
         the application can only be access via a VPN.
      -  :green_circle: ``public`` - This indicates to Amadla that the
         application can be access via the web without the need of using
         a VPN nor is it just internal.

+-------+--------------+----------------+--------------+-------------+
| Name  | Local server | Internal       | Need VPN for | Anyone      |
|       | access       | server access  | access       |             |
+=======+==============+================+==============+=============+
| :r    | :heavy       |                |              |             |
| ed_ci | _check_mark: |                |              |             |
| rcle: |              |                |              |             |
| prot  |              |                |              |             |
| ected |              |                |              |             |
+-------+--------------+----------------+--------------+-------------+
| :yell | :heavy       | :hea           |              |             |
| ow_ci | _check_mark: | vy_check_mark: |              |             |
| rcle: |              |                |              |             |
| int   |              |                |              |             |
| ernal |              |                |              |             |
+-------+--------------+----------------+--------------+-------------+
| :lar  | :heavy       | :hea           | :heavy       |             |
| ge_bl | _check_mark: | vy_check_mark: | _check_mark: |             |
| ue_ci |              |                |              |             |
| rcle: |              |                |              |             |
| pr    |              |                |              |             |
| ivate |              |                |              |             |
+-------+--------------+----------------+--------------+-------------+
| :gre  | :heavy       | :hea           | :heavy       | :heavy_     |
| en_ci | _check_mark: | vy_check_mark: | _check_mark: | check_mark: |
| rcle: |              |                |              |             |
| p     |              |                |              |             |
| ublic |              |                |              |             |
+-------+--------------+----------------+--------------+-------------+

:open_book: ``README.md``
'''''''''''''''''''''''''

::

   # Plugin Name
   Application Plugin Name (link to the website of the application/service).

   ![Screenshot](http://url_to_project_screenshot) This is optional.

   The screenshot is practicle if you have a web interface that communicates what the application is about.

   ## How to use
   ...

   ## Screenshots
   This section is optional, but encouraged if one screenshot doesn't tell the whole story. Just a list of images, one per line. We do the resizing, so use actual size screenshots.

   ![Screenshot 1](http://url_to_project_screenshot)
   ![Screenshot 2](http://url_to_project_screenshot)
   ![Screenshot 3](http://url_to_project_screenshot)
   ![Screenshot 4](http://url_to_project_screenshot)

   ## Arbitrary section
   This is an arbitrary section. You can have as many of these as you want.
   Some arbitrary section examples:

   * FAQ
   * Notes
   * Misc
   * Known issues

   The name is up to you, but remember to keep it meaningful, short and simple. If it is very verbose and detailed please use the `docs/` directory. Arbitrary sections are always optional.

Server
^^^^^^

The server configurations use `Ansible <https://www.ansible.com/>`__ to
install all the packages and other components that are needed. It also
takes care of all the settings of SELinux and other Linux
configurations.

**Environment variables:** - ``USER_USERNAME`` -
``USER_SERVER_PASSWORD``

Cloud
^^^^^

The cloud configurations use `Packer <https://www.packer.io/>`__\ …

Image Builder
~~~~~~~~~~~~~

Here is the bash script of the container that runs the builder:

.. code:: bash

   #!/usr/bin/env bash

   podman run --rm -it \
           -v /etc/localtime:/etc/localtime:ro \
           -v ./entry.sh:/home/entry.sh \
           -v ./plugins/packer-builder-vultr:/root/.packer.d/plugins/packer-builder-vultr \
           -v ./plugins/packer-builder-vultr:/bin/packer-builder-vultr \
           -v ./clouds.d/:/home/clouds.d/ \
           -v ./ansible/base/:/home/ansible/ \
           -v ./.vault:/home/.vault \
           -v ~/.ssh/id_ed25519.pub:/home/.ssh/id_ed25519.pub \
           -v ~/.ssh/id_ed25519:/home/.ssh/id_ed25519 \
           -e "GET_INFO=${GET_INFO}" \
           -e "CLOUD_SERVICE=${CLOUD_SERVICE}" \
           -e "VAULT_ADDRESS=${VAULT_ADDRESS}" \
           -e "USER_ID=${USER_ID}" \
           -e "USER_USERNAME=jn" \
           -e "USER_SERVER_PASSWORD=amadlatest" \
           -e "SERVICE_PROFILE=default" \
           -e "PACKER_LOG=${PACKER_LOG}" \
           --net host \
           --name image-builder \
           image-builder

Volumes
^^^^^^^

-  ``/etc/localtime:/etc/localtime:ro`` -
-  ``./entry.sh:/home/entry.sh`` -
-  ``./plugins/packer-builder-vultr:/root/.packer.d/plugins/packer-builder-vultr``
-  ``./plugins/packer-builder-vultr:/bin/packer-builder-vultr``
-  ``./clouds.d/:/home/clouds.d/`` -
-  ``./ansible/base/:/home/ansible/`` -
-  ``./.vault:/home/.vault`` -
-  ``~/.ssh/id_ed25519.pub:/home/.ssh/id_ed25519.pub`` -
-  ``~/.ssh/id_ed25519:/home/.ssh/id_ed25519`` -

Environment variables
^^^^^^^^^^^^^^^^^^^^^

-  ``GET_INFO=${GET_INFO}`` - It’s a call for info about
-  ``CLOUD_SERVICE=${CLOUD_SERVICE}`` - Pass the name of the cloud you
   want to execute (maybe change to a *volume*\ …)
-  ``VAULT_ADDRESS=${VAULT_ADDRESS}`` - The Vault address (in local
   environment: http://127.0.0.1:1234/). The value comes from Vault
   after it starts, you will only need to copy paste the command given
   by it.
-  ``USER_ID=${USER_ID}`` - [STRIKEOUT:This is for storing and
   retrieving the secrets of a particular user (this is useful if you
   have multiple users using Amadla)] **DEPRECATED** Instead you will
   use: `Userpass \|
   Vault <https://developer.hashicorp.com/vault/docs/auth/userpass>`__ +
   `Identity: Entities and Groups \|
   Vault <https://developer.hashicorp.com/vault/tutorials/auth-methods/identity>`__
   + `Manage Authentication Methods \|
   Vault <https://developer.hashicorp.com/vault/tutorials/getting-started-ui/getting-started-auth-ui>`__
-  ``USER_USERNAME=jn`` - It is the username for the SSH of the server
   (needs a better name… Seriously!) NOTE -> Used in Ansible
-  ``USER_SERVER_PASSWORD=amadlatest`` - Password for the SSH of the
   server (needs also a better name… Very serious!) -> Used in Ansible
-  ``SERVICE_PROFILE=default`` - No idea
-  ``PACKER_LOG=${PACKER_LOG}`` - Log level?? Maybe… No idea

``config/containers/image-builder/entry.sh``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Is the container main entry point bash script
-  It also calls with ``curl`` the Vault server to get the secrets
   needed to connect to the cloud service

**Vault path:**

``"${VAULT_ADDRESS}/${VAULT_API_VERSION}/secret/data/${CLOUD_SERVICE}/credentials/${SERVICE_PROFILE}"``

-  ``VAULT_ADDRESS`` - Is the same value that is pass by the ``run.sh``
   script
-  ``VAULT_API_VERSION`` - (Maybe added to ``run.sh``??) - For now it is
   hardcoded in the ``entry.sh`` script it is required in the HTTP API
   enpoint path
-  ``CLOUD_SERVICE`` - Since you can have multiple cloud services the
   storage in Vault is devided by cloud providers
-  ``SERVICE_PROFILE`` - Not sure why it’s called that and it’s also
   because they might be different credentials based on what you are
   using it from e.g. Prod, Staging, etc

Step by step
~~~~~~~~~~~~

-  ``entry.sh`` - The entrypoint for the container
-  Call to Vault to get the secrets to connect to the cloud service API
-  ``build.sh`` - Simple bash function that calls another script named
   ``creds.sh`` and then calls (with the credential from ``creds.sh``)
   the secrets needed to execute ``packer build`` that will execute the
   packer script
-  ``creds.sh`` - Calls Vault to get secret uses the bash function in
   the ``entry.sh`` and populates a environment variable that will later
   be used as source of the secret or secrets to communicated with the
   API of the cloud service
-  ``<cloud service name>.base.pkr.hcl`` - The Packer script
-  Ansible is called inside the Packer script (depending on the server
   type you configure it will load the one you set in the configuration
   file)

..

   @TODO: Add Terraform… For now this is only for generating an server
   image.

Unit Testing
------------

The command to run the Python unit test:

.. code:: bash

   python3 -m unittest tests/test_*.py

The unit tests are found ``./tests/`` directory.

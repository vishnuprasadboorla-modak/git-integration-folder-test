# Command-Line-Interface

[![PyPI version](https://badge.fury.io/py/yeedu-cli.svg)](https://badge.fury.io/py/yeedu-cli)

CLI(Command Line Interface) is a standard CLI to run interactively with Yeedu's [RESTful-API](https://github.com/yeedu-io/RESTful-API).

# CLI Features

- [CLI Setup](#cli-setup)
  - [Windows](#windows)
    - [Generate Executable file for yeedu CLI](#generate-executable-file-for-yeedu-cli)
  - [Linux](#linux)
  - [Environment Variable Setup](#environment-variable-setup)
  - [Authentication Setup](#authentication-setup)
    - [Storing the credentials as Environment Variables](#storing-the-credentials-as-environment-variables)
    - [Storing the credentials inside a `yeedu_credentials.config` file](#storing-the-credentials-inside-a-yeedu_credentialsconfig-file)
    - [Storing the Yeedu Session Token inside a file](#storing-the-yeedu-session-token-inside-a-file)
    - [Configure](#configure)
    - [list-tenants](#list-tenants)
    - [associate-tenant](#associate-tenant)
- [Resource](#resource)
  - [Lookup](#lookup)
    - [list-providers](#list-providers)
    - [get-provider](#get-provider)
    - [list-provider-availability-zones](#list-provider-availability-zones)
    - [get-provider-availability-zone](#get-provider-availability-zone)
    - [list-provider-machine-types](#list-provider-machine-types)
    - [get-provider-machine-type](#get-provider-machine-type)
    - [list-disk-machine-types](#list-disk-machine-types)
    - [list-credential-types](#list-credential-types)
    - [list-engine-cluster-instance-status](#list-engine-cluster-instance-status)
    - [list-spark-compute-types](#list-spark-compute-types)
    - [list-spark-infra-versions](#list-spark-infra-versions)
    - [list-spark-job-status](#list-spark-job-status)
    - [list-workflow-execution-states](#list-workflow-execution-states)
    - [list-workflow-types](#list-workflow-types)
    - [list-linux-distros](#list-linux-distros)
  - [Volume Configuration](#volume-configuration)
    - [create-volume-conf](#create-volume-conf)
    - [list-volume-confs](#list-volume-confs)
    - [search-volume-confs](#search-volume-confs)
    - [get-volume-conf](#get-volume-conf)
    - [edit-volume-conf](#edit-volume-conf)
    - [delete-volume-conf](#delete-volume-conf)
  - [Network Configuration](#network-configuration)
    - [create-network-conf](#create-network-conf)
    - [list-network-confs](#list-network-confs)
    - [search-network-confs](#search-network-confs)
    - [get-network-conf](#get-network-conf)
    - [edit-network-conf](#edit-network-conf)
    - [delete-network-conf](#delete-network-conf)
  - [Boot Disk Image Config](#boot-disk-image-config)
    - [create-boot-disk-image-conf](#create-boot-disk-image-conf)
    - [get-boot-disk-image-conf](#get-boot-disk-image-conf)
    - [list-boot-disk-image-confs](#list-boot-disk-image-confs)
    - [search-boot-disk-image-confs](#search-boot-disk-image-confs)
    - [edit-boot-disk-image-conf](#edit-boot-disk-image-conf)
    - [delete-boot-disk-image-conf](#delete-boot-disk-image-conf)
  - [Credentials Configuration](#credentials-configuration)
    - [create-credential-conf](#create-credential-conf)
    - [list-credential-confs](#list-credential-confs)
    - [search-credential-confs](#search-credential-confs)
    - [get-credential-conf](#get-credential-conf)
    - [edit-credential-conf](#edit-credential-conf)
    - [delete-credential-conf](#delete-credential-conf)
  - [Cloud Env](#cloud-env)
    - [create-cloud-env](#create-cloud-env)
    - [list-cloud-envs](#list-cloud-envs)
    - [search-cloud-envs](#search-cloud-envs)
    - [get-cloud-env](#get-cloud-env)
    - [edit-cloud-env](#edit-cloud-env)
    - [delete-cloud-env](#delete-cloud-env)
  - [Object Storage Manager](#object-storage-manager)
    - [create-object-storage-manager](#create-object-storage-manager)
    - [list-object-storage-managers](#list-object-storage-managers)
    - [search-object-storage-managers](#search-object-storage-managers)
    - [get-object-storage-manager](#get-object-storage-manager)
    - [edit-object-storage-manager](#edit-object-storage-manager)
    - [delete-object-storage-manager](#delete-object-storage-manager)
  - [Object Storage Manager Files](#object-storage-manager-files)
    - [create-object-storage-manager-file](#create-object-storage-manager-file)
    - [list-object-storage-manager-files](#list-object-storage-manager-files)
    - [search-object-storage-manager-files](#search-object-storage-manager-files)
    - [get-object-storage-manager-file](#get-object-storage-manager-file)
    - [delete-object-storage-manager-file](#delete-object-storage-manager-file)
- [Cluster](#cluster)
  - [Cluster Configuration](#cluster-configuration)
    - [create-conf](#create-conf)
    - [list-confs](#list-confs)
    - [search-confs](#search-confs)
    - [get-conf](#get-conf)
    - [edit-conf](#edit-conf)
    - [delete-conf](#delete-conf)
  - [Cluster Instance](#cluster-instance)
    - [create](#create)
    - [list](#list)
    - [search](#search)
    - [get](#get)
    - [edit](#edit)
    - [start](#start)
    - [stop](#stop)
    - [destroy](#destroy)
    - [disable](#disable)
    - [enable](#enable)
    - [get-stats](#get-stats)
    - [stop-all-jobs](#stop-all-jobs)
    - [list-errors](#list-errors)
    - [list-status](#list-status)
    - [logs](#logs)
  - [Cluster Access Control](#cluster-access-control)
    - [associate-workspace](#associate-workspace)
    - [dissociate-workspace](#dissociate-workspace)
    - [list-workspaces](#list-workspaces)
    - [list-workspace-clusters](#list-workspace-clusters)
    - [search-workspace-clusters](#search-workspace-clusters)
- [Workspace](#workspace)
  - [Worksapce](#workspace)
    - [create](#create-1)
    - [list](#list-1)
    - [search](#search-1)
    - [get](#get-1)
    - [get-stats](#get-stats-1)
    - [edit](#edit-1)
    - [enable](#enable)
    - [disable](#disable)
    - [export](#export)
    - [import](#import)
  - [Worksapce Files](#workspace-Files)
    - [create-workspace-file](#create-workspace-files)
    - [list-workspace-files](#list-workspace-files)
    - [search-workspace-files](#search-workspace-files)
    - [get-workspace-file](#get-workspace-file)
    - [delete-workspace-file](#delete-workspace-file)
    - [download-workspace-file](#download-workspace-file)
    - [rename-workspace-file](#rename-workspace-file)
    - [get-workspace-files-usage](#get-workspace-files-usage)
    - [move-workspace-file](#move-workspace-file)
    - [copy-workspace-file](#copy-workspace-file)
  - [Workspace Access Control](#workspace-access-control)
    - [create-user-access](#create-user-access)
    - [create-group-access](#create-group-access)
    - [delete-user-access](#delete-user-access)
    - [delete-group-access](#delete-group-access)
    - [list-users](#list-users)
    - [search-users](#search-users)
    - [match-user](#match-user)
    - [list-groups](#list-groups)
    - [search-groups](#search-groups)
    - [match-group](#match-group)
    - [get-user-access](#get-user-access)
    - [get-group-access](#get-group-access)
    - [list-users-access](#list-users-access)
    - [search-users-access](#search-users-access)
    - [list-groups-access](#list-groups-access)
    - [search-groups-access](#search-groups-access)
- [Job](#job)
  - [Spark Job](#spark-job)
    - [create](#create-2)
    - [list](#list-2)
    - [search](#search-2)
    - [get](#get-2)
    - [edit](#edit-2)
    - [enable](#enable-1)
    - [disable](#disable-1)
    - [export](#export-2)
  - [Spark Job Runs](#spark-job-runs)
    - [start](#start-1)
    - [list-runs](#list-runs)
    - [search-runs](#search-runs)
    - [get-run](#get-run)
    - [stop](#stop-1)
    - [run-status](#run-status)
    - [logs](#logs-1)
  - [Workflow Details By Spark Job Application Id](#workflow-details-by-spark-job-application-id)
    - [get-workflow-job-instance](#get-workflow-job-instance)
- [Notebook](#notebook)
  - [Notebook](#notebook-1)
    - [create](#create-3)
    - [list](#list-3)
    - [search](#search-3)
    - [get](#get-3)
    - [edit](#edit-3)
    - [enable](#enable-3)
    - [disable](#disable-3)
    - [export](#export-2)
  - [Notebook Runs](#notebook-runs)
    - [start](#start-2)
    - [kernel-start](#kernel-start)
    - [kernel-status](#kernel-status)
    - [kernel-interrupt](#kernel-interrupt)
    - [kernel-restart](#kernel-restart)
    - [list-runs](#list-runs-1)
    - [search-runs](#search-runs-2)
    - [get-run](#get-run-2)
    - [stop](#stop-2)
    - [logs](#logs-2)
- [Billing](#billing)
  - [tenants](#tenants)
  - [date-range](#date-range)
  - [clusters](#clusters)
  - [machine-types](#machine-types)
  - [labels](#labels)
  - [usage](#usage)
  - [invoice](#invoice)
- [IAM](#iam-identity-and-access-management)
  - [User](#user)
    - [search-tenants](#search-tenants)
    - [get-user-info](#get-user-info)
    - [get-user-roles](#get-user-roles)
  - [Shared Platform and Admin](#shared-platform-and-admin)
    - [sync-user](#sync-user)
    - [sync-group](#sync-group)
    - [list-user-groups](#list-user-groups)
    - [list-users](#list-users-1)
    - [search-users](#search-users-1)
    - [match-user](#match-user-1)
    - [list-group-users](#list-group-users)
    - [list-groups](#list-groups-1)
    - [search-groups](#search-groups-1)
    - [match-group](#match-group-1)
  - [Lookup](#lookup-1)
    - [list-resources](#list-resources)
    - [get-resource](#get-resource)
    - [list-permissions](#list-permissions)
    - [get-permission](#get-permission)
    - [list-roles](#list-roles)
    - [get-role](#get-role)
    - [list-rules](#list-rules)
    - [get-rule](#get-rule)
    - [list-workspace-permissions](#list-workspace-permissions)
    - [get-workspace-permission](#get-workspace-permission)
- [Platform-Admin](#platform-admin)
  - [Tenant](#tenant)
    - [create-tenant](#create-tenant)
    - [list-tenants](#list-tenants-1)
    - [search-tenants](#search-tenants-1)
    - [get-tenant](#get-tenant)
    - [edit-tenant](#edit-tenant)
    - [delete-tenant](#delete-tenant)
  - [User](#user-1)
    - [list-user-tenants](#list-user-tenants)
    - [list-tenant-users](#list-tenant-users)
    - [search-tenant-users](#search-tenant-users)
    - [get-tenant-user](#get-tenant-user)
    - [get-user-roles](#get-user-roles-1)
    - [list-users-roles](#list-users-roles)
    - [get-role-users](#get-role-users)
    - [create-user-role](#create-user-role)
    - [delete-user-role](#delete-user-role)
  - [Group](#group)
    - [list-tenant-groups](#list-tenant-groups)
    - [search-tenant-groups](#search-tenant-groups)
    - [get-tenant-group](#get-tenant-group)
    - [get-group-roles](#get-group-roles)
    - [list-groups-roles](#list-groups-roles)
    - [get-role-groups](#get-role-groups)
    - [create-group-role](#create-group-role)
    - [delete-group-role](#delete-group-role)
- [Admin](#admin)
  - [User](#user-2)
    - [list-users](#list-users-2)
    - [search-users](#search-users-2)
    - [get-user](#get-user)
    - [get-user-roles](#get-user-roles-2)
    - [list-users-roles](#list-users-roles-1)
    - [get-role-users](#get-role-users-1)
    - [create-user-role](#create-user-role-1)
    - [delete-user-role](#delete-user-role-1)
  - [Group](#group-1)
    - [list-groups](#list-groups-2)
    - [search-groups](#search-groups-2)
    - [get-group](#get-group)
    - [get-group-roles](#get-group-roles-1)
    - [list-groups-roles](#list-groups-roles-1)
    - [get-role-groups](#get-role-groups-1)
    - [create-group-role](#create-group-role-1)
    - [delete-group-role](#delete-group-role-1)
- [Token](#token)
  - [create](#create-2)
  - [list](#list-4)
  - [delete](#delete)
- [Secrets](#secret)
  - [Tenant Secrets](#tenant-secrets)
    - [create](#create-tenant-secret)
    - [edit](#edit-tenant-secret)
    - [delete](#delete-tenant-secret)
  - [User Secrets](#user-secrets)
    - [create](#create-user-secret)
    - [edit](#edit-user-secret)
    - [delete](#delete-user-secret)
  - [Workspace Secrets](#workspace-secrets)
    - [create](#create-workspace-secret)
    - [edit](#edit-workspace-secret)
    - [delete](#delete-tenant-secret)
- [Metastore Catalog Operations](#metastore-catalog-operations)
  - [Secret Management](#secret-management)
    - [Associate Secret](#associate-secret)
    - [Update Associated Secrets](#update-associated-secrets)
    - [Deassociate Secret (Unlink)](#deassociate-secret-unlink)
    - [List Associated Secrets](#list-associated-secrets)
  - [Catalog Types](#catalog-types)
    - [List Metastore Catalogs](#list-metastore-catalogs)
    - [Search Metastore Catalogs](#search-metastore-catalogs)
    - [Databricks Unity](#databricks-unity)
      - [Create](#databricks-unity-create)
      - [Edit](#databricks-unity-edit)
      - [Delete](#databricks-unity-delete)
    - [Hive](#hive)
      - [Create](#hive-create)
      - [Edit](#hive-edit)
      - [Delete](#hive-delete)
    - [Glue Catalog](#glue-catalog)
      - [Create](#glue-catalog-create)
      - [Edit](#glue-catalog-edit)
      - [Delete](#glue-catalog-delete)
- [Catalog Explorer](#catalog-explorer)
  - [List Catalogs](#list-catalogs)
  - [List Schemas](#list-schemas)
  - [List Tables](#list-tables)
  - [List Columns](#list-columns)
  - [List Table Summaries](#list-table-summaries)
  - [Get Table DDL](#get-table-ddl)
  - [List Functions](#list-functions)
  - [List Volumes](#list-volumes)
- [Git Credentials](#git-credentials)
  - [Create](#create-git-credential)
  - [List](#list-git-credentials)
  - [Get](#get-git-credential)
  - [Edit](#edit-git-credential)
  - [Delete](#delete-git-credential)
- [Git](#git)
  - [Clone](#clone)
  - [List Branches](#list-branches)
  - [Create Branch](#create-branch)
  - [Switch Branch](#switch-branch)
  - [Status](#status)
  - [Stage Files](#stage-files)
  - [File Diff](#file-diff)
  - [Commit & Push](#commit-push)
  - [Pull](#pull)
  - [Clone Status](#clone-status)
  - [Clone Log](#clone-log)
  - [Clone Errors](#clone-errors)
  - [Discard Changes](#discard-changes)
---
# CLI Setup

To set up the Yeedu CLI on the environment, execute the following command from the project directory.

## Windows

```cmd
pip install --editable .
```

### Generate Executable file for Yeedu CLI

- Need to install `pyinstaller` using below-mentioned command

```cmd
pip install pyinstaller
```

- From the project directory execute the mention command

```cmd
pyinstaller --onefile yeedu.py
```

Traverse to `\dist` directory and get the executable file `yeedu.exe`

- The yeedu.exe commands can be formed as shown below:

```cmd
yeedu.exe [-h]
yeedu.exe <command> [-h]
yeedu.exe <command> <subcommand> [-h]
```

- Example of Yeedu CLI command using the executable file

```cmd
yeedu.exe resource list-providers
```

## Linux

- WSL

```bash
sudo apt install python3-pip
```

```bash
pip3 install --editable .
```

- Bash

```bash
sudo python3 setup.py develop
```

### Tab-Autocomplete

- Navigate to the `/scripts` directory from the project directory and obtain the `yeedu_autocompletion.sh` file.

```bash
# Add the following to ~/.bashrc
source /path/to/yeedu_autocompletion.sh
```

- After adding the above information to `~/.bashrc`, restart the shell or open a new shell session.

## Environment Variable Setup

Create a `.env` file in the project directory and provide below environment variables.

```bash
# Below mentioned values are the default values of Environment Variables
YEEDU_RESTAPI_URL="http://localhost:8080"
YEEDU_CLI_LOG_DIR="/.yeedu/cli/logs/"
YEEDU_USERNAME=USER
YEEDU_PASSWORD=PASS
YEEDU_RESTAPI_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFiY2RlZiIsImlkIjoiMSIsImlhdCI6MTY2NzgwOTYwMX0.HwhdTHBttnR0NFtmUDjcxTLMSLfyNuBs7t7GO9zOf08
YEEDU_RESTAPI_TOKEN_FILE_PATH="/home/user/yeedu_cli.config"
YEEDU_CLI_VERIFY_SSL=true

# Provide the YEEDU_SSL_CERT_FILE path if YEEDU_CLI_VERIFY_SSL is set to true.
YEEDU_SSL_CERT_FILE="/home/user/crt"
```

Alternative of `.env` file

- Windows CMD

```cmd
SET YEEDU_RESTAPI_URL="http://localhost:8080"
SET YEEDU_CLI_LOG_DIR=/.yeedu/cli/logs/
SET YEEDU_USERNAME=USER
SET YEEDU_PASSWORD=PASS
SET YEEDU_RESTAPI_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFiY2RlZiIsImlkIjoiMSIsImlhdCI6MTY2NzgwOTYwMX0.HwhdTHBttnR0NFtmUDjcxTLMSLfyNuBs7t7GO9zOf08
SET YEEDU_RESTAPI_TOKEN_FILE_PATH=/home/user/yeedu_cli.config
SET YEEDU_CLI_VERIFY_SSL=true

# Provide the YEEDU_SSL_CERT_FILE path if YEEDU_CLI_VERIFY_SSL is set to true.
SET YEEDU_SSL_CERT_FILE="/home/user/crt"
```

- Linux

```bash
export YEEDU_RESTAPI_URL="http://localhost:8080"
export YEEDU_CLI_LOG_DIR="/.yeedu/cli/logs/"
export YEEDU_USERNAME=USER
export YEEDU_PASSWORD=PASS
export YEEDU_RESTAPI_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFiY2RlZiIsImlkIjoiMSIsImlhdCI6MTY2NzgwOTYwMX0.HwhdTHBttnR0NFtmUDjcxTLMSLfyNuBs7t7GO9zOf08
export YEEDU_RESTAPI_TOKEN_FILE_PATH="/home/user/yeedu_cli.config"
export YEEDU_CLI_VERIFY_SSL=true

# Provide the YEEDU_SSL_CERT_FILE path if YEEDU_CLI_VERIFY_SSL is set to true.
export YEEDU_SSL_CERT_FILE="/home/user/crt"
```

## Authentication Setup

- The following describes the ways of storing credentials, which will be used to generate the token [Environment Variables being given priority].

### Storing the credentials as Environment Variables

```env
YEEDU_USERNAME=USER
YEEDU_PASSWORD=PASS
```

### Storing the credentials inside a `yeedu_credentials.config` file

- The yeedu_credentials.config file needs to be created inside the directory `home/user/.yeedu/` which consists of JSON as shown below:

```JSON
{
  "YEEDU_USERNAME": "USER",
  "YEEDU_PASSWORD": "PASS"
}
```

### Storing the Yeedu Session Token inside a file

- If the user is already having the Yeedu Session Token. The user can save the token at any location and provide the file path in environment variable `YEEDU_RESTAPI_TOKEN_FILE_PATH`
  - For example `YEEDU_RESTAPI_TOKEN_FILE_PATH="/home/user/Documents/YeeduToken/{FileName}"`
- The format to store the token is as shown below:

```JSON
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJpYXQiOjE2ODg3MjA0MjIsImV4cCI6MTY4ODg5MzIyMn0.EfxuXKPBISQB4ep-sPQbo6R7tg2irlnAC_krqnuXJ5Q"
}
```

| Command Name                          | Utility                                                        |
| ------------------------------------- | -------------------------------------------------------------- |
| [configure](#configure)               | Used to generate the token.                                    |
| [list-tenants](#list-tenants)         | To list all the available tenants for the session user.        |
| [associate-tenant](#associate-tenant) | To associate the tenant with the current user's session Token. |

### Configure

```bash
yeedu configure -h
```

```bash
Yeedu CLI

positional arguments:
  {configure}

options:
  -h, --help            Show this help message and exit.
  --timeout [TIMEOUT]   Provide token expiration timeout Example: --timeout=24h 
                        or 2 days or 1700s,--timeout=infinity 
                        (infinity for no expiration time) 
                        to generate Yeedu Token. (default: 48h)
  --no-browser [{true,false}]
                        If 'no-browser=true' is provided, the browser will not open
                        automatically for the SSO login URL. (default: false)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- User can provide the file path to store the configured token using the environment variable `YEEDU_RESTAPI_TOKEN_FILE_PATH`.
  - For example `YEEDU_RESTAPI_TOKEN_FILE_PATH="/home/user/Documents/YeeduToken/{FileName}"`
- configure example with the optional argument passed.

```bash
yeedu configure --timeout=72h
```

- Console output

```bash
{
  "message": "The token has been configured for the username: USER and stored at location: /home/user/.yeedu/yeedu_cli.config"
}
```

The generated token will be used internally for accessing the yeedu features based on the acess level provided to the given username

- To list the tenants a user has access to, execute the `yeedu iam list-tenants` command.

### list-tenants

```bash
yeedu iam list-tenants -h
```

```bash
usage:  list-tenants [-h] [--page_number PAGE_NUMBER] [--limit LIMIT]
                     [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --page_number PAGE_NUMBER
                        Specifies the page number for the items to return. (default: 1)
  --limit LIMIT         Specifies the numbers of items to return. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- list-tenants example without optional arguments passed.

```bash
yeedu iam list-tenants
```

- Console output

```bash
{
  "data": [
    {
      "tenant_id": "6423f466-ff56-4ba4-8c2d-8229beb67e38",
      "name": "tenant1",
      "description": "Yeedu Tenant 1"
    },
    {
      "tenant_id": "066a702d-6b9d-4176-afc5-51c24a651739",
      "name": "tenant2",
      "description": "Yeedu Tenant 2"
    },
    {
      "tenant_id": "cf1f945f-01ce-4ac6-a070-8c733f2fa791",
      "name": "tenant3",
      "description": "Yeedu Tenant 3"
    },
    {
      "tenant_id": "6b682ef1-ede4-4d96-bab6-cd008aadd534",
      "name": "tenant4",
      "description": "Yeedu Tenant 4"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 4,
    "total_pages": 1,
    "limit": 100
  }
}
```

- Execute `yeedu iam associate-tenant --tenant_id={tenant_id}` to associate a tenant id from the `yeedu iam list-tenants` response to the session token.

### associate-tenant

```bash
yeedu iam associate-tenant -h
```

```bash
usage:  associate-tenant [-h] --tenant_id TENANT_ID [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide tenant_id to associate it with session token
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- associate-tenant example with required argument '--tenant_id' passed.

```bash
yeedu iam associate-tenant --tenant_id="6423f466-ff56-4ba4-8c2d-8229beb67e38"
```

- Console output

```bash
{
  "message": "Successfully associated Tenant"
}
```

# Resource

## Lookup

| Command Name                                                                | Utility                                                                              |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [list-providers](#list-providers)                                           | To get information about all Cloud Providers.                                        |
| [get-provider](#get-provider)                                               | To get information about a specific Cloud Provider.                                  |
| [list-provider-availability-zones](#list-provider-availability-zones)       | To get information about Availability Zones for a specific Cloud Provider.           |
| [get-provider-availability-zone](#get-provider-availability-zone)           | To get information about a specific Availability Zone for a specific Cloud Provider. |
| [list-provider-machine-types](#list-provider-machine-types)                 | To get information about Machine Types for a specific Cloud Provider.                |
| [get-provider-machine-type](#get-provider-machine-type)                     | To get information about a specific Machine Type for a specific Cloud Provider.      |
| [list-disk-machine-types](#list-disk-machine-types)                         | To get information about all disk machine types.                                     |
| [list-credential-types](#list-credential-types)                             | To get information about all credential types.                                       |
| [list-engine-cluster-instance-status](#list-engine-cluster-instance-status) | To get information about all available engine cluster instance status.               |
| [list-spark-compute-types](#list-spark-compute-types)                       | To get information about all spark compute types.                                    |
| [list-spark-infra-versions](#list-spark-infra-versions)                     | To get information about spark infra version.                                        |
| [list-spark-job-status](#list-spark-job-status)                             | To get information about spark job status.                                           |
| [list-workflow-execution-states](#list-workflow-execution-states)           | To get information about workflow execution state.                                   |
| [list-workflow-types](#list-workflow-types)                                 | To get information about workflow type.                                              |

### list-providers

```bash
yeedu resource list-providers -h
```

```bash
usage:  list-providers [-h] [--json-output [{pretty,default}]]
                       [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-providers example without any optional argument passed for output format.

```bash
yeedu resource list-providers
```

- Console output

```bash
[
  {
    "cloud_provider_id": "0",
    "name": "GCP",
    "description": "Provider for creating infrastructure on Google Cloud Platform",
    "from_date": "2023-09-27T06:11:53.179Z",
    "to_date": null
  },
  {
    "cloud_provider_id": "1",
    "name": "AWS",
    "description": "Provider for creating infrastructure on Amazon Web Services",
    "from_date": "2023-09-27T06:11:53.179Z",
    "to_date": null
  },
  {
    "cloud_provider_id": "2",
    "name": "Azure",
    "description": "Provider for creating infrastructure on Azure Cloud Platform",
    "from_date": "2023-09-27T06:11:53.179Z",
    "to_date": null
  }
]
```

### get-provider

```bash
yeedu resource get-provider -h
```

```bash
usage:  get-provider [-h] --cloud_provider_id CLOUD_PROVIDER_ID
                     [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider_id CLOUD_PROVIDER_ID
                        Provide specific cloud provider id to get-provider.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-provider example with required '--cloud_provider_id' argument passed.

```bash
yeedu resource get-provider --cloud_provider_id=0
```

- Console output

```bash
{
  "cloud_provider_id": "0",
  "name": "GCP",
  "description": "Provider for creating infrastructure on Google Cloud Platform",
  "from_date": "2023-09-27T06:11:53.179Z",
  "to_date": null
}
```

### list-provider-availability-zones

```bash
yeedu resource list-provider-availability-zones -h
```

```bash
usage:  list-provider-availability-zones [-h] --cloud_provider_id CLOUD_PROVIDER_ID [--limit LIMIT] [--page_number PAGE_NUMBER]
                                         [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider_id CLOUD_PROVIDER_ID
                        Provide specific Cloud Provider id to list-provider-availability-zones.
  --limit LIMIT         Provide limit to list number of availability zones. (default: 100)
  --page_number PAGE_NUMBER
                        To list availability zones for a specific page_number. (default: 1)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-provider-availability-zones example with required '--cloud_provider_id' argument passed.

```bash
yeedu resource list-provider-availability-zones --cloud_provider_id=0 --limit=2
```

- Console output

```bash
{
"data": [
  {
    "availability_zone_id": "0",
    "cloud_provider": {
      "cloud_provider_id": 0,
      "name": "GCP",
      "description": "Provider for creating infrastructure on Google Cloud Platform"
    },
    "name": "asia-east1-a",
    "region": "asia-east1",
    "description": "Changhua County, Taiwan, APAC",
    "from_date": "2023-09-27T06:11:53.246Z",
    "to_date": null
  },
  ...
  {
    "availability_zone_id": "102",
    "cloud_provider": {
      "cloud_provider_id": 0,
      "name": "GCP",
      "description": "Provider for creating infrastructure on Google Cloud Platform"
    },
    "name": "us-south1-c",
    "region": "us-south1",
    "description": "Dallas, Texas, North America",
    "from_date": "2023-09-27T06:11:53.246Z",
    "to_date": null
  }
],
  "result_set": {
    "current_page": 1,
    "total_objects": 102,
    "total_pages": 103,
    "limit": 1,
    "next_page": 2
  }
}
```

### get-provider-availability-zone

```bash
yeedu resource get-provider-availability-zone -h
```

```bash
usage:  get-provider-availability-zone [-h] --cloud_provider_id CLOUD_PROVIDER_ID
                                       --availability_zone_id AVAILABILITY_ZONE_ID
                                       [--json-output [{pretty,default}]]
                                       [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider_id CLOUD_PROVIDER_ID
                        Provide specific cloud provider id to get-provider-
                        availability-zone.
  --availability_zone_id AVAILABILITY_ZONE_ID
                        Provide specific Availability Zone id to get-provider-
                        availability-zone.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-provider-availability-zone example with required arguments passed.

```bash
yeedu resource get-provider-availability-zone --cloud_provider_id=1 --availability_zone_id=116
```

- Console output

```bash
{
  "availability_zone_id": "116",
  "cloud_provider": {
    "name": "AWS",
    "description": "Provider for creating infrastructure on Amazon Web Services"
  },
  "name": "ca-central-1",
  "region": "ca-central-1",
  "description": "central, Canada",
  "from_date": "2024-06-06T07:55:47.752Z",
  "to_date": null
}
```

### list-provider-machine-types

```bash
yeedu resource list-provider-machine-types -h
```

```bash
usage:  list-provider-machine-types [-h] --cloud_provider_id CLOUD_PROVIDER_ID [--limit LIMIT] [--page_number PAGE_NUMBER]
                                    [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider_id CLOUD_PROVIDER_ID
                        Provide specific cloud provider id to list-provider-machine-types.
  --limit LIMIT         Provide limit to list number of machine types. (default: 100)
  --page_number PAGE_NUMBER
                        To list machine types for a specific page_number. (default: 1)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-provider-machine-types example with required '--cloud_provider_id' argument passed.

```bash
yeedu resource list-provider-machine-types --cloud_provider_id=0
```

- Console output

```bash
{
  "data": [
    {
      "machine_type_id": 2,
      "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP",
        "description": "Provider for creating infrastructure on Google Cloud Platform"
      },
      "name": "n2-highcpu-16",
      "vCPUs": 16,
      "memory": "16 GiB",
      "has_cuda": false,
      "gpu_model": null,
      "gpus": 0,
      "gpu_memory": null,
      "cpu_model": [
        "Intel Xeon Scalable (Ice Lake) 3rd Generation",
        "Intel Xeon Scalable (Cascade Lake) 2nd Generation"
      ],
      "cpu_min_frequency_GHz": [
        "2.6",
        "2.8"
      ],
      "cpu_max_frequency_GHz": [
        "3.5",
        "3.9"
      ],
      "has_local_disk": false,
      "local_disk_size_GB": null,
      "local_num_of_disks": null,
      "local_disk_bus_type": null,
      "local_disk_throughput_MB": null,
      "machine_price_ycu": 5.6,
      "from_date": "2024-06-06T07:55:47.735016+00:00",
      "to_date": "infinity"
    },
    {
      "machine_type_id": 1,
      "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP",
        "description": "Provider for creating infrastructure on Google Cloud Platform"
      },
      "name": "n1-highcpu-16",
      "vCPUs": 16,
      "memory": "14.4 GiB",
      "has_cuda": false,
      "gpu_model": null,
      "gpus": 0,
      "gpu_memory": null,
      "cpu_model": [
        "Intel Xeon Scalable (Skylake) 1st Generation",
        "Intel Xeon E5 v4 (Broadwell E5)",
        "Intel Xeon E5 v3 (Haswell)",
        "Intel Xeon E5 v2 (Ivy Bridge)",
        "Intel Xeon E5 (Sandy Bridge)"
      ],
      "cpu_min_frequency_GHz": [
        "2.0",
        "2.2",
        "2.3",
        "2.5",
        "2.6"
      ],
      "cpu_max_frequency_GHz": [
        "3.5",
        "3.7",
        "3.8",
        "3.5",
        "3.6"
      ],
      "has_local_disk": false,
      "local_disk_size_GB": null,
      "local_num_of_disks": null,
      "local_disk_bus_type": null,
      "local_disk_throughput_MB": null,
      "machine_price_ycu": 5.44,
      "from_date": "2024-06-06T07:55:47.735016+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 48,
    "total_pages": 24,
    "limit": 2,
    "next_page": 2
  }
}
```

### get-provider-machine-type

```bash
yeedu resource get-provider-machine-type -h
```

```bash
usage:  get-provider-machine-type [-h] --cloud_provider_id CLOUD_PROVIDER_ID
                                  --machine_type_id MACHINE_TYPE_ID
                                  [--json-output [{pretty,default}]]
                                  [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider_id CLOUD_PROVIDER_ID
                        Provide specific cloud provider id to get-provider-machine-type.
  --machine_type_id MACHINE_TYPE_ID
                        Provide specific machine type id to get-provider-machine-type.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-provider-machine-type example with all the required arguments passed.

```bash
yeedu resource get-provider-machine-type --cloud_provider_id=0 --machine_type_id=1
```

- Console output

```bash
{
  "machine_type_id": 1,
  "cloud_provider": {
    "cloud_provider_id": 0,
    "name": "GCP",
    "description": "Provider for creating infrastructure on Google Cloud Platform"
  },
  "name": "n1-highcpu-16",
  "vCPUs": 16,
  "memory": "14.4 GiB",
  "has_cuda": false,
  "gpu_model": null,
  "gpus": 0,
  "gpu_memory": null,
  "cpu_model": [
    "Intel Xeon Scalable (Skylake) 1st Generation",
    "Intel Xeon E5 v4 (Broadwell E5)",
    "Intel Xeon E5 v3 (Haswell)",
    "Intel Xeon E5 v2 (Ivy Bridge)",
    "Intel Xeon E5 (Sandy Bridge)"
  ],
  "cpu_min_frequency_GHz": [
    "2.0",
    "2.2",
    "2.3",
    "2.5",
    "2.6"
  ],
  "cpu_max_frequency_GHz": [
    "3.5",
    "3.7",
    "3.8",
    "3.5",
    "3.6"
  ],
  "has_local_disk": false,
  "local_disk_size_GB": null,
  "local_num_of_disks": null,
  "local_disk_bus_type": null,
  "local_disk_throughput_MB": null,
  "machine_price_ycu": 5.44,
  "from_date": "2024-06-06T07:55:47.735016+00:00",
  "to_date": "infinity"
}
```

### list-disk-machine-types

```bash
yeedu resource list-disk-machine-types -h
```

```bash
usage:  list-disk-machine-types [-h] [--json-output [{pretty,default}]]
                                [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-disk-machine-types example without optional arguments passed for the output format.

```bash
yeedu resource list-disk-machine-types
```

- Console output

```bash
[
  {
    "disk_type_id": "0",
    "cloud_provider": {
      "name": "GCP",
      "description": "Provider for creating infrastructure on Google Cloud Platform"
    },
    "name": "pd-ssd",
    "has_fixed_size": false,
    "min_size": 10,
    "max_size": 64000,
    "from_date": "2023-09-27T06:11:53.242Z",
    "to_date": null
  },
  ...
  {
    "disk_type_id": "8",
    "cloud_provider": {
      "name": "Azure",
      "description": "Provider for creating infrastructure on Azure Cloud Platform"
    },
    "name": "Premiumv2_LRS",
    "has_fixed_size": false,
    "min_size": 1,
    "max_size": 65536,
    "from_date": "2024-06-06T07:55:47.750Z",
    "to_date": null
  }
]
```

### list-credential-types

```bash
yeedu resource list-credential-types -h
```

```bash
usage:  list-credential-types [-h] [--cloud_provider [{GCP,AWS,Azure}]] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider [{GCP,AWS,Azure}]
                        Provide specific cloud_provider to get information about related credential types.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-credential-types example without optional argument passed for output format.

```bash
yeedu resource list-credential-types
```

- Console output

```bash
[
  {
    "credential_type_id": 0,
    "name": "Google Service Account",
    "cloud_provider": {
      "cloud_provider_id": 0,
      "name": "GCP",
      "description": "Provider for creating infrastructure on Google Cloud Platform"
    },
    "from_date": "2024-05-29T16:09:48.788269+00:00",
    "to_date": "infinity"
  },
  {
    "credential_type_id": 1,
    "name": "AWS Access Secret Key Pair",
    "cloud_provider": {
      "cloud_provider_id": 1,
      "name": "AWS",
      "description": "Provider for creating infrastructure on Amazon Web Services"
    },
    "from_date": "2024-05-29T16:09:48.788269+00:00",
    "to_date": "infinity"
  },
  {
    "credential_type_id": 2,
    "name": "Azure Service Principal",
    "cloud_provider": {
      "cloud_provider_id": 2,
      "name": "Azure",
      "description": "Provider for creating infrastructure on Azure Cloud Platform"
    },
    "from_date": "2024-05-29T16:09:48.788269+00:00",
    "to_date": "infinity"
  }
]
```

### list-engine-cluster-instance-status

```bash
yeedu resource list-engine-cluster-instance-status -h
```

```bash
usage:  list-engine-cluster-instance-status [-h] [--json-output [{pretty,default}]]
                                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-engine-cluster-instance-status example without optional arguments passed for the output format.

```bash
yeedu resource list-engine-cluster-instance-status
```

- Console output

```bash
[
  {
    "engine_cluster_instance_status_id": "0",
    "name": "INITIATING",
    "description": "Cluster will be eventually created",
    "from_date": "2023-09-27T06:11:53.186Z",
    "to_date": null
  },
  ...
  {
    "engine_cluster_instance_status_id": "8",
    "name": "RESIZING_DOWN",
    "description": "The cluster instance will scale down",
    "from_date": "2023-09-27T06:11:53.186Z",
    "to_date": null
  }
]
```

### list-spark-compute-types

```bash
yeedu resource list-spark-compute-types -h
```

```bash
usage:  list-spark-compute-types [-h] [--json-output [{pretty,default}]]
                                 [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-spark-compute-types example without optional arguments passed for the output format.

```bash
yeedu resource list-spark-compute-types
```

- Console output

```bash
[
  {
    "spark_compute_type_id": "0",
    "name": "YEEDU",
    "description": null,
    "from_date": "2023-09-27T06:11:53.265Z",
    "to_date": null
  }
]
```

### list-spark-infra-versions

```bash
yeedu resource list-spark-infra-versions -h
```

```bash
usage:  list-spark-infra-versions [-h] [--json-output [{pretty,default}]]
                                  [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-spark-infra-versions example without optional arguments passed for the output format.

```bash
yeedu resource list-spark-infra-versions
```

- Console output

```bash
[
  {
    "spark_infra_version_id": "0",
    "spark_docker_image_name": "2.4.8",
    "spark_version": "2.4.8",
    "hive_version": "3.2.3",
    "hadoop_version": "2.10.1",
    "scala_version": "2.11.12",
    "python_version": "2.7.18",
    "notebook_support": false,
    "has_cuda_support": false,
    "thrift_support": true,
    "yeedu_functions_support": true,
    "from_date": "2024-06-06T07:55:47.731Z",
    "to_date": null
  },
  {
    "spark_infra_version_id": "1",
    "spark_docker_image_name": "v3.2.2-20",
    "spark_version": "3.2.2",
    "hive_version": "3.2.3",
    "hadoop_version": "3.2.4",
    "scala_version": "2.12.15",
    "python_version": "3.9.5",
    "notebook_support": true,
    "has_cuda_support": true,
    "thrift_support": true,
    "yeedu_functions_support": true,
    "from_date": "2024-06-06T07:55:47.731Z",
    "to_date": null
  },
  {
    "spark_infra_version_id": "2",
    "spark_docker_image_name": "v3.3.4-3",
    "spark_version": "3.3.4",
    "hive_version": "3.2.3",
    "hadoop_version": "3.2.4",
    "scala_version": "2.12.15",
    "python_version": "3.9.5",
    "notebook_support": true,
    "has_cuda_support": false,
    "thrift_support": true,
    "yeedu_functions_support": true,
    "from_date": "2024-06-06T07:55:47.731Z",
    "to_date": null
  }
]
```

### list-spark-job-status

```bash
yeedu resource list-spark-job-status -h
```

```bash
usage:  list-spark-job-status [-h] [--json-output [{pretty,default}]]
                              [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-spark-job-status example without optional arguments passed for the output format.

```bash
yeedu resource list-spark-job-status
```

- Console output

```bash
[
  {
    "spark_job_status_id": "0",
    "name": "SUBMITTED",
    "description": "Job was submitted, waiting for Application ID",
    "from_date": "2023-09-27T06:11:53.266Z",
    "to_date": null
  },
  ...
  {
    "spark_job_status_id": "8",
    "name": "STOPPED",
    "description": "The process was successfully stopped",
    "from_date": "2023-09-27T06:11:53.266Z",
    "to_date": null
  }
]
```

### list-workflow-execution-states

```bash
yeedu resource list-workflow-execution-states -h
```

```bash
usage:  list-workflow-execution-states [-h] [--json-output [{pretty,default}]]
                                       [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-workflow-execution-states example without optional arguments passed for the output format.

```bash
yeedu resource list-workflow-execution-states
```

- Console output

```bash
[
  {
    "workflow_execution_state_id": -1,
    "name": "NONE",
    "description": "NONE",
    "from_date": "2023-09-27T06:11:53.255Z",
    "to_date": null
  },
  ...
  {
    "workflow_execution_state_id": 99,
    "name": "DONE",
    "description": "NONE",
    "from_date": "2023-09-27T06:11:53.255Z",
    "to_date": null
  }
]
```

### list-workflow-types

```bash
yeedu resource list-workflow-types -h
```

```bash
usage:  list-workflow-types [-h] [--json-output [{pretty,default}]]
                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-workflow-types example without optional arguments passed for the output format.

```bash
yeedu resource list-workflow-types
```

- Console output

```bash
[
  {
    "workflow_type_id": "0",
    "name": "spark_start",
    "queue_name": "yeedu.workflows.usi.start",
    "description": null,
    "from_date": "2023-09-27T06:11:53.257Z",
    "to_date": null
  },
  ...
  {
    "workflow_type_id": "8",
    "name": "cosi_resize_down",
    "queue_name": "yeedu.workflows.cosi",
    "description": null,
    "from_date": "2023-09-27T06:11:53.257Z",
    "to_date": null
  }
]
```

### list-linux-distros

```bash
yeedu resource list-linux-distros -h
```

```bash
usage:  list-linux-distros [-h] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-workflow-types example without optional argument passed for output format.

```bash
yeedu resource list-linux-distros
```

- Console output

```bash
[
  {
    "linux_distro_id": 2,
    "distro_name": "RHEL",
    "distro_version": "8",
    "from_date": "2024-05-29T16:09:48.784Z",
    "to_date": null
  },
  {
    "linux_distro_id": 1,
    "distro_name": "UBUNTU",
    "distro_version": "22.04 LTS",
    "from_date": "2024-05-29T16:09:48.784Z",
    "to_date": null
  },
  {
    "linux_distro_id": 0,
    "distro_name": "UBUNTU",
    "distro_version": "20.04 LTS",
    "from_date": "2024-05-29T16:09:48.784Z",
    "to_date": null
  }
]
```

## Volume Configuration

| Command Name                                | Utility                                                   |
| ------------------------------------------- | --------------------------------------------------------- |
| [create-volume-conf](#create-volume-conf)   | To create the Volume Configuration.                       |
| [list-volume-confs](#list-volume-confs)     | To list all the available Volume Configurations.          |
| [search-volume-confs](#search-volume-confs) | To search all the available Volume Configurations.        |
| [get-volume-conf](#get-volume-conf)         | To get information about a specific Volume Configuration. |
| [edit-volume-conf](#edit-volume-conf)       | To edit a specific Volume Configuration.                  |
| [delete-volume-conf](#delete-volume-conf)   | To delete a specific Volume Configuration.                |

### create-volume-conf

```bash
yeedu resource create-volume-conf -h
```

```bash
usage:  create-volume-conf [-h] --name [NAME] [--description [DESCRIPTION]] --encrypted {true,false} [--size [SIZE]] --disk_type_id DISK_TYPE_ID
                           --machine_volume_num MACHINE_VOLUME_NUM --machine_volume_strip_num MACHINE_VOLUME_STRIP_NUM [--disk_iops DISK_IOPS]
                           [--disk_throughput_MB DISK_THROUGHPUT_MB] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name [NAME]         Provide name to create-volume-conf.
  --description [DESCRIPTION]
                        Provide description to create-volume-conf.
  --encrypted {true,false}
                        Provide encrypted to create-volume-conf.
  --size [SIZE]         Provide size to create-volume-conf.
  --disk_type_id DISK_TYPE_ID
                        Provide disk_type to create-volume-conf.
  --machine_volume_num MACHINE_VOLUME_NUM
                        Provide machine_volume_num to create-volume-conf.
  --machine_volume_strip_num MACHINE_VOLUME_STRIP_NUM
                        Provide machine_volume_strip_num to create-volume-conf.
  --disk_iops DISK_IOPS
                        Provide disk_iops to create-volume-conf.
  --disk_throughput_MB DISK_THROUGHPUT_MB
                        Provide disk_throughput_MB to create-volume-conf.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-volume-conf example with all the required arguments passed.

```bash
yeedu resource create-volume-conf --name="yeedu_volume" --encrypted=false --disk_type_id=2  --machine_volume_num=1 --machine_volume_strip_num=1
```

- Console output

```bash
{
  "volume_conf_id": "1",
  "name": "yeedu_volume",
  "description": null,
  "encrypted": false,
  "size": "375",
  "disk_type_id": "2",
  "disk_type_name": "local-ssd",
  "machine_volume_num": 1,
  "machine_volume_strip_num": 1,
  "disk_iops": null,
  "disk_throughput_MB": null,
  "created_by_user_id": "1",
  "modified_by__user_id": "1",
  "last_update_date": "2023-07-20T10:57:08.387Z",
  "from_date": "2023-07-20T10:57:08.387Z",
  "to_date": null
}
```

### list-volume-confs

```bash
yeedu resource list-volume-confs -h
```

```bash
usage:  list-volume-confs [-h] [--cloud_provider [{GCP,AWS,Azure}]] [--page_number PAGE_NUMBER] [--limit LIMIT]
                          [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider [{GCP,AWS,Azure}]
                        To list volume configurations for a specific cloud provider.
  --page_number PAGE_NUMBER
                        To list Volume Configurations for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of Volume Configurations. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-volume-confs example with optional arguments passed for the output format.

```bash
yeedu resource list-volume-confs --cloud_provider="GCP"
```

- Console output

```bash
{
  "data": [
  {
      "volume_conf_id": 1,
      "name": "yeedu_volume",
      "description": null,
      "encrypted": true,
      "size": 375,
      "disk_type": {
        "disk_type_id": 2,
        "cloud_provider": {
          "cloud_provider_id": 0,
          "name": "GCP"
      },
      },
      "machine_volume_num": 1,
      "machine_volume_strip_num": 1,
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-01-05T09:27:59.407362+00:00",
      "from_date": "2024-01-05T09:27:59.407362+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-volume-confs

```bash
yeedu resource search-volume-confs -h
```

```bash
usage:  search-volume-confs [-h] --volume_conf_name VOLUME_CONF_NAME [--page_number PAGE_NUMBER] [--limit LIMIT]
                            [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --volume_conf_name VOLUME_CONF_NAME
                        Provide volume_conf_name to search all the available Volume Configurations.
  --page_number PAGE_NUMBER
                        To search Volume Configurations for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of Volume Configurations. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-volume-confs example with required argument '--volume_conf_name' passed.

```bash
yeedu resource search-volume-confs --volume_conf_name="yeedu_"
```

- Console output

```bash
{
  "data": [
    {
      "volume_conf_id": 1,
      "name": "yeedu_volume",
      "description": null,
      "encrypted": false,
      "size": 375,
      "disk_type": {
        "disk_type_id": 4,
        "name": "local-ssd",
        "has_fixed_size": true,
        "min_size": 375,
        "max_size": 375
      },
      "machine_volume_num": 1,
      "machine_volume_strip_num": 1,
      "disk_iops": null,
      "disk_throughput_MB": null,
      "created_by": null,
      "modified_by": null,
      "last_update_date": "2024-05-29T16:09:48.824776+00:00",
      "from_date": "2024-05-29T16:09:48.824776+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-volume-conf

```bash
yeedu resource get-volume-conf -h
```

```bash
usage:  get-volume-conf [-h] [--volume_conf_id VOLUME_CONF_ID] [--volume_conf_name VOLUME_CONF_NAME] [--json-output [{pretty,default}]]
                        [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --volume_conf_id VOLUME_CONF_ID
                        Provide volume_conf_id to get information about a specific Volume Configuration.
  --volume_conf_name VOLUME_CONF_NAME
                        Provide volume_conf_name to get information about a specific Volume Configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-volume-conf example with the required argument '--volume_conf_id' passed.

```bash
yeedu resource get-volume-conf --volume_conf_id=1
```

- Console output

```bash
{
  "volume_conf_id": 1,
  "name": "yeedu_volume",
  "description": null,
  "encrypted": true,
  "size": 375,
  "disk_type": {
    "disk_type_id": 2,
    "cloud_provider": {
      "cloud_provider_id": 0,
      "name": "GCP"
    },
    "name": "local-ssd",
    "has_fixed_size": true,
    "min_size": 375,
    "max_size": 375
  },
  "machine_volume_num": 1,
  "machine_volume_strip_num": 1,
  "disk_iops": null,
  "disk_throughput_MB": null,
  "created_by": null,
  "modified_by": null,
  "last_update_date": "2024-05-29T16:09:48.824776+00:00",
  "from_date": "2024-05-29T16:09:48.824776+00:00",
  "to_date": "infinity"
}
```

### edit-volume-conf

```bash
yeedu resource edit-volume-conf -h
```

```bash
usage:  edit-volume-conf [-h] [--volume_conf_id VOLUME_CONF_ID] [--volume_conf_name VOLUME_CONF_NAME] [--name [NAME]]
                         [--description [DESCRIPTION]] [--encrypted [{true,false}]] [--disk_type_id DISK_TYPE_ID] [--size [SIZE]]
                         [--machine_volume_num MACHINE_VOLUME_NUM] [--machine_volume_strip_num MACHINE_VOLUME_STRIP_NUM] [--disk_iops DISK_IOPS]
                         [--disk_throughput_MB DISK_THROUGHPUT_MB] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --volume_conf_id VOLUME_CONF_ID
                        Provide specific volume_conf_id to edit-volume-conf.
  --volume_conf_name VOLUME_CONF_NAME
                        Provide specific volume_conf_name to edit-volume-conf.
  --name [NAME]         Provide name to edit-volume-conf.
  --description [DESCRIPTION]
                        Provide description to edit-volume-conf.
  --encrypted [{true,false}]
                        Provide encrypted to edit-volume-conf.
  --disk_type_id DISK_TYPE_ID
                        Provide disk_type to edit-volume-conf.
  --size [SIZE]         Provide size to edit-volume-conf.
  --machine_volume_num MACHINE_VOLUME_NUM
                        Provide machine_volume_num to edit-volume-conf.
  --machine_volume_strip_num MACHINE_VOLUME_STRIP_NUM
                        Provide machine_volume_strip_num to edit-volume-conf.
  --disk_iops DISK_IOPS
                        Provide disk_iops to edit-volume-conf.
  --disk_throughput_MB DISK_THROUGHPUT_MB
                        Provide disk_throughput_MB to edit-volume-conf.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- edit-volume-conf example with the required '--volume_conf_id' argument and other optional argument is passed which is to be updated.

```bash
yeedu resource edit-volume-conf --volume_conf_id=1 --encrypted=true
```

- Console output

```bash
{
  "volume_conf_id": "1",
  "name": "yeedu_volume",
  "description": null,
  "encrypted": true,
  "size": "375",
  "disk_type_id": "2",
  "disk_type_name": "local-ssd",
  "machine_volume_num": 1,
  "machine_volume_strip_num": 1,
  "disk_iops": null,
  "disk_throughput_MB": null,
  "created_by_user_id": "1",
  "modified_by__user_id": "1",
  "last_update_date": "2023-07-20T10:57:08.387Z",
  "from_date": "2023-07-20T10:57:08.387Z",
  "to_date": null
}
```

### delete-volume-conf

```bash
yeedu resource delete-volume-conf -h
```

```bash
usage:  delete-volume-conf [-h] [--volume_conf_id VOLUME_CONF_ID] [--volume_conf_name VOLUME_CONF_NAME] [--json-output [{pretty,default}]]
                           [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --volume_conf_id VOLUME_CONF_ID
                        Provide volume_conf_id to delete a specific Volume Configuration.
  --volume_conf_name VOLUME_CONF_NAME
                        Provide volume_conf_name to delete a specific Volume Configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- delete-volume-conf example with any one of the required argument '--volume_conf_name' which is to be deleted.

```bash
yeedu resource delete-volume-conf --volume_conf_id=1
```

- Console output

```bash
{
  "message": "Deleted machine volume configuration ID: 1."
}
```

## Network Configuration

| Command Name                                  | Utility                                                                                  |
| --------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [create-network-conf](#create-network-conf)   | To create the Network Configuration.                                                     |
| [list-network-confs](#list-network-confs)     | To get information about Network Configurations for a specific Cloud Provider.           |
| [search-network-confs](#search-network-confs) | To search information about Network Configurations.                                      |
| [get-network-conf](#get-network-conf)         | To get information about a specific Network Configuration for a specific Cloud Provider. |
| [edit-network-conf](#edit-network-conf)       | To edit a specific Network Configuration based on cloud provider Id and network Id.      |
| [delete-network-conf](#delete-network-conf)   | To delete a specific Network Configuration.                                              |

### create-network-conf

```bash
yeedu resource create-network-conf -h
```

```bash
usage:  create-network-conf [-h] --name NAME [--description DESCRIPTION] --network_project_id NETWORK_PROJECT_ID --network_name NETWORK_NAME
                            --subnet SUBNET --availability_zone_id AVAILABILITY_ZONE_ID [--network_tags ['value1,value2']]
                            [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name NAME           Provide name to create-network-conf.
  --description DESCRIPTION
                        Provide description to create-network-conf.
  --network_project_id NETWORK_PROJECT_ID
                        Provide network_project_id to create-network-conf.
  --network_name NETWORK_NAME
                        Provide network_name to create-network-conf.
  --subnet SUBNET       Provide subnet to create-network-conf.
  --availability_zone_id AVAILABILITY_ZONE_ID
                        Provide availability_zone_id to create-network-conf.
  --network_tags ['value1,value2']
                        Provide network_tags to create-network-conf. (default: [])
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-network-conf example with all the required and optional arguments passed.

```bash
yeedu resource create-network-conf --name="yeedu_network" --network_project_id="yeedu" --network_name='yeedu-spark-vpc' --subnet='custom-subnet--yeedu' --availability_zone_id=75
```

- Console output

```bash
{
  "name":"yeedu_network",
  "description": null,
  "network_conf_id": "1",
  "network_project_id": "yeedu",
  "network_name": "yeedu-spark-vpc",
  "subnet": "subnet-yeedu",
  "availability_zone_id": "75",
  "tenant_id": "0b5017a9-6099-497f-81ba-d4e537e23538",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-05-30T07:59:26.316752+00:00",
  "from_date": "2024-05-30T07:59:26.316752+00:00",
  "to_date": null
}
```

### list-network-confs

```bash
yeedu resource list-network-confs -h
```

```bash
usage:  list-network-confs [-h] [--cloud_provider [{GCP,AWS,Azure}]] [--page_number PAGE_NUMBER] [--limit LIMIT]
                           [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider [{GCP,AWS,Azure}]
                        Provide specific cloud_provider to get information about related Network Configurations.
  --page_number PAGE_NUMBER
                        To list Network Configurations for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of Network Configurations. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-network-confs example with the `--cloud_provider` optional arguments passed.

```bash
yeedu resource list-network-confs --cloud_provider="GCP"
```

- Console output

```bash
{
  "data": [
    {
      "network_conf_id": "1",
      "network_conf_name": "yeedu_network",
      "description": null,
      "network_project_id": "yeedu",
      "network_name": "yeedu-spark-vpc",
      "network_tags": [
          "yeedu"
        ],
      "subnet": "subnet-yeedu",
      "availability_zone": {
        "cloud_provider": {
            "cloud_provider_id": 0,
            "name": "GCP",
            "description": "Provider for creating infrastructure on Google Cloud Platform"
          },
        "name": "us-central1-a",
        "region": "us-central1",
        "description": "Council Bluffs, Iowa, North America"
      },
      "tenant_id": "0b5017a9-6099-497f-81ba-d4e537e23538",
      "created_by": {
        "user_id": "1",
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": "1",
        "username": "YSU0000"
      },
      "last_update_date": "2024-05-30T07:59:26.316752+00:00",
      "from_date": "2024-05-30T07:59:26.316752+00:00",
      "to_date": null
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-network-confs

```bash
yeedu resource search-network-confs -h
```

```bash
usage:  search-network-confs [-h] --network_conf_name NETWORK_CONF_NAME [--cloud_provider [{GCP,AWS,Azure}]] [--page_number PAGE_NUMBER]
                             [--limit LIMIT] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --network_conf_name NETWORK_CONF_NAME
                        Provide network_conf_name to search Network Configuration.
  --cloud_provider [{GCP,AWS,Azure}]
                        Provide specific cloud_provider to search about related Network Configurations.
  --page_number PAGE_NUMBER
                        To search Network Configurations for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of Network Configurations. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-network-confs example with the required argument `--network_conf_name` and `--cloud_provider` optional arguments passed.

```bash
yeedu resource search-network-confs --network_conf_name="yeedu" --cloud_provider="GCP"
```

- Console output

```bash
{
  "data": [
    {
      "network_conf_id": "1",
      "network_conf_name": "yeedu_network",
      "description": null,
      "network_project_id": "yeedu",
      "network_name": "yeedu-spark-vpc",
      "network_tags": [
          "yeedu"
        ],
      "subnet": "custom-subnet--yeedu",
      "availability_zone": {
        "cloud_provider": {
            "cloud_provider_id": 0,
            "name": "GCP",
            "description": "Provider for creating infrastructure on Google Cloud Platform"
          },
        "name": "us-central1-a",
        "region": "us-central1",
        "description": "Council Bluffs, Iowa, North America"
      },
      "tenant_id": "0b5017a9-6099-497f-81ba-d4e537e23538",
      "created_by": {
        "user_id": "1",
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": "1",
        "username": "YSU0000"
      },
      "last_update_date": "2024-05-30T07:59:26.316752+00:00",
      "from_date": "2024-05-30T07:59:26.316752+00:00",
      "to_date": null
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-network-conf

```bash
yeedu resource get-network-conf -h
```

```bash
usage:  get-network-conf [-h] [--network_conf_id NETWORK_CONF_ID] [--network_conf_name NETWORK_CONF_NAME] [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --network_conf_id NETWORK_CONF_ID
                        Provide network_conf_id to get information about a specific network Configuration.
  --network_conf_name NETWORK_CONF_NAME
                        Provide network_conf_name to get information about a specific network Configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-network-conf example with the required '--network_conf_id' argument passed.

```bash
yeedu resource get-network-conf --network_conf_id=1
```

- Console output

```bash
{
  "network_conf_id": "1",
  "network_conf_name": "yeedu_network",
  "description": null,
  "network_project_id": "yeedu",
  "network_name": "yeedu-spark-vpc",
  "network_tags": [
      "yeedu"
    ],
  "subnet": "custom-subnet--yeedu",
  "availability_zone": {
    "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP",
        "description": "Provider for creating infrastructure on Google Cloud Platform"
      },
    "name": "us-central1-a",
    "region": "us-central1",
    "description": "Council Bluffs, Iowa, North America"
  },
  "tenant_id": "0b5017a9-6099-497f-81ba-d4e537e23538",
  "created_by": {
    "user_id": "1",
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": "1",
    "username": "YSU0000"
  },
  "last_update_date": "2024-05-30T07:59:26.316752+00:00",
  "from_date": "2024-05-30T07:59:26.316752+00:00",
  "to_date": null
}
```

### edit-network-conf

```bash
yeedu resource edit-network-conf -h
```

```bash
usage:  edit-network-conf [-h] [--network_conf_id NETWORK_CONF_ID] [--network_conf_name NETWORK_CONF_NAME] [--name NAME]
                          [--description DESCRIPTION] [--network_name [NETWORK_NAME]] [--network_project_id [NETWORK_PROJECT_ID]]
                          [--availability_zone_id AVAILABILITY_ZONE_ID] [--subnet [SUBNET]] [--network_tags ['value1,value2']]
                          [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --network_conf_id NETWORK_CONF_ID
                        Provide a specific Network Configuration network_conf_id to edit-network-conf.
  --network_conf_name NETWORK_CONF_NAME
                        Provide a specific Network Configuration network_conf_name to edit-network-conf.
  --name NAME           Provide name to edit-network-conf.
  --description DESCRIPTION
                        Provide description to edit-network-conf.
  --network_name [NETWORK_NAME]
                        Provide network_name to edit-network-conf.
  --network_project_id [NETWORK_PROJECT_ID]
                        Provide network_project_id to edit-network-conf.
  --availability_zone_id AVAILABILITY_ZONE_ID
                        Provide availability_zone_id to edit-network-conf.
  --subnet [SUBNET]     Provide subnet to edit-network-conf.
  --network_tags ['value1,value2']
                        Provide network_tags to edit-network-conf.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- edit-network-conf example with the required '--network_conf_id' and '--cloud_provider_id' argument and other optional argument is passed which is to be updated.

```bash
yeedu resource edit-network-conf --network_conf_id=1 --network_name="yeedu-spark-vpc"
```

- Console output

```bash
{
  "name":"yeedu_network",
  "description": null,
  "network_conf_id": "1",
  "network_project_id": "yeedu",
  "network_name": "yeedu-spark-vpc",
  "subnet": "custom-subnet--yeedu",
  "availability_zone_id": "75",
  "tenant_id": "0b5017a9-6099-497f-81ba-d4e537e23538",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-05-30T07:59:26.316752+00:00",
  "from_date": "2024-05-30T07:59:26.316752+00:00",
  "to_date": null
}
```

### delete-network-conf

```bash
yeedu resource delete-network-conf -h
```

```bash
usage:  delete-network-conf [-h] [--network_conf_id NETWORK_CONF_ID] [--network_conf_name NETWORK_CONF_NAME] [--json-output [{pretty,default}]]
                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --network_conf_id NETWORK_CONF_ID
                        Provide network_conf_id to delete a specific network Configuration.
  --network_conf_name NETWORK_CONF_NAME
                        Provide network_conf_name to delete a specific network Configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- delete-network-conf example with the required '--network_conf_id' argument.

```bash
yeedu resource delete-network-conf --network_conf_id=1
```

- Console output

```bash
{
  "message": "Deleted network configuration ID: 1."
}
```

## Boot Disk Image Config

| Command Name                                                  | Utility                                                                |
| ------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [create-boot-disk-image-conf](#create-boot-disk-image-conf)   | To create a Boot Disk Image Configuration.                             |
| [get-boot-disk-image-conf](#get-boot-disk-image-conf)         | To get the information about a specific Boot Disk Image Configuration. |
| [list-boot-disk-image-confs](#list-boot-disk-image-confs)     | To list all the available Boot Disk Image Configurations.              |
| [search-boot-disk-image-confs](#search-boot-disk-image-confs) | To search all the available boot disk image configurations.            |
| [edit-boot-disk-image-conf](#edit-boot-disk-image-conf)       | To edit a specific boot disk image configuration.                      |
| [delete-boot-disk-image-conf](#delete-boot-disk-image-conf)   | To delete a specific boot disk image configuration.                    |

### create-boot-disk-image-conf

```bash
yeedu resource create-boot-disk-image-conf -h
```

```bash
usage:  create-boot-disk-image-conf [-h] --name NAME [--description DESCRIPTION] --cloud_provider_id CLOUD_PROVIDER_ID --linux_distro_id
                                    LINUX_DISTRO_ID --boot_disk_image BOOT_DISK_IMAGE [--json-output [{pretty,default}]]
                                    [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name NAME           Provide name to create-boot-disk-image-conf.
  --description DESCRIPTION
                        Provide description to create-boot-disk-image-conf.
  --cloud_provider_id CLOUD_PROVIDER_ID
                        Provide cloud_provider_id to create-boot-disk-image-conf.
  --linux_distro_id LINUX_DISTRO_ID
                        Provide linux_distro_id to create-boot-disk-image-conf.
  --boot_disk_image BOOT_DISK_IMAGE
                        Provide boot_disk_image to create-boot-disk-image-conf.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-boot-disk-image-conf example with all the required arguments passed.

```bash
yeedu resource create-boot-disk-image-conf --name="gcp_ubuntu" --cloud_provider_id=0 --linux_distro_id=0 --boot_disk_image="ubuntu-os-cloud/ubuntu-2004-lts"
```

- Console output

```bash
{
  "boot_disk_image_id": "2",
  "boot_disk_image_name": "yeedu_boot_disk_image",
  "description": null,
  "cloud_provider_id": 0,
  "linux_distro_id": 1,
  "boot_disk_image": "ubuntu-os-cloud/ubuntu-2004-lts",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-05-29T16:09:48.84463+00:00",
  "from_date": "2024-05-29T16:09:48.84463+00:00",
  "to_date": null
}
```

### get-boot-disk-image-conf

```bash
yeedu resource get-boot-disk-image-conf -h
```

```bash
usage:  get-boot-disk-image-conf [-h] [--boot_disk_image_id BOOT_DISK_IMAGE_ID] [--boot_disk_image_name BOOT_DISK_IMAGE_NAME]
                                 [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --boot_disk_image_id BOOT_DISK_IMAGE_ID
                        Provide Boot Disk Image Id to get information about a specific boot disk image configuration.
  --boot_disk_image_name BOOT_DISK_IMAGE_NAME
                        Provide Boot Disk Image Name to get information about a specific boot disk image configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-boot-disk-image-conf example with required arguments passed.

```bash
yeedu resource get-boot-disk-image-conf --boot_disk_image_id=1
```

- Console output

```bash
{
  "boot_disk_image_id": 1,
  "boot_disk_image_name": "gcp_ubuntu",
  "description": "Base image for GCP Ubuntu",
  "cloud_provider": {
    "cloud_provider_id": 0,
    "name": "GCP",
    "description": "Provider for creating infrastructure on Google Cloud Platform"
  },
  "linux_distro": {
    "linux_distro_id": 0,
    "distro_name": "UBUNTU",
    "distro_version": "20.04 LTS"
  },
  "boot_disk_image": "ubuntu-os-cloud/ubuntu-2004-lts",
  "created_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "last_update_date": "2024-05-29T16:09:48.84463+00:00",
  "from_date": "2024-05-29T16:09:48.84463+00:00",
  "to_date": "infinity"
}
```

### list-boot-disk-image-confs

```bash
yeedu resource list-boot-disk-image-confs -h
```

```bash
usage:  list-boot-disk-image-confs [-h] [--cloud_provider [{GCP,AWS,Azure}]] [--page_number PAGE_NUMBER] [--limit LIMIT]
                                   [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider [{GCP,AWS,Azure}]
                        Provide cloud_provider to list all the related boot disk image configs for a specific Cloud Provider.
  --page_number PAGE_NUMBER
                        To list boot disk image configurations for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of boot disk image configurations. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-boot-disk-image-confs example with an optional argument passed.

```bash
yeedu resource list-boot-disk-image-confs --cloud_provider="GCP"
```

- Console output

```bash
{
  "data": [
    {
      "boot_disk_image_id": 1,
      "boot_disk_image_name": "gcp_ubuntu",
      "description": "Base image for GCP Ubuntu",
      "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP",
        "description": "Provider for creating infrastructure on Google Cloud Platform"
      },
      "linux_distro": {
        "linux_distro_id": 0,
        "distro_name": "UBUNTU",
        "distro_version": "20.04 LTS"
      },
      "boot_disk_image": "ubuntu-os-cloud/ubuntu-2004-lts",
      "created_by": {
      "user_id": "1",
      "username": "YSU0000"
      },
      "modified_by": {
        "user_id": "1",
        "username": "YSU0000"
      },
      "last_update_date": "2024-05-29T16:09:48.84463+00:00",
      "from_date": "2024-05-29T16:09:48.84463+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 52,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-boot-disk-image-confs

```bash
yeedu resource search-boot-disk-image-confs -h
```

```bash
usage:  search-boot-disk-image-confs [-h] --boot_disk_image_name
                                     BOOT_DISK_IMAGE_NAME
                                     [--cloud_provider [{GCP,AWS,Azure}]]
                                     [--page_number PAGE_NUMBER]
                                     [--limit LIMIT]
                                     [--json-output [{pretty,default}]]
                                     [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --boot_disk_image_name BOOT_DISK_IMAGE_NAME
                        Provide Boot Disk Image Name to search information about all the related boot disk image configs.
  --cloud_provider [{GCP,AWS,Azure}]
                        Provide cloud_provider to search all the related boot disk image configs for a specific Cloud Provider.
  --page_number PAGE_NUMBER
                        To list boot disk image configurations for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of boot disk image configurations. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-boot-disk-image-confs example with the required argument '--boot_disk_image_name' passed.

```bash
yeedu resource search-boot-disk-image-confs --boot_disk_image_name="yeedu_"
```

- Console output

```bash
{
  "data": [
    {
      "boot_disk_image_id": 1,
      "boot_disk_image_name": "yeedu_boot_disk_image",
      "description": "Base image for GCP Ubuntu",
      "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP",
        "description": "Provider for creating infrastructure on Google Cloud Platform"
      },
      "linux_distro": {
        "linux_distro_id": 0,
        "distro_name": "UBUNTU",
        "distro_version": "20.04 LTS"
      },
      "boot_disk_image": "ubuntu-os-cloud/ubuntu-2004-lts",
      "created_by": {
      "user_id": "1",
      "username": "YSU0000"
      },
      "modified_by": {
        "user_id": "1",
        "username": "YSU0000"
      },
      "last_update_date": "2024-05-29T16:09:48.84463+00:00",
      "from_date": "2024-05-29T16:09:48.84463+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 52,
    "total_pages": 1,
    "limit": 100
  }
}
```

### edit-boot-disk-image-conf

```bash
yeedu resource edit-boot-disk-image-conf -h
```

```bash
usage:  edit-boot-disk-image-conf [-h] [--boot_disk_image_id BOOT_DISK_IMAGE_ID] [--boot_disk_image_name BOOT_DISK_IMAGE_NAME] [--name NAME]
                                  [--description DESCRIPTION] [--linux_distro_id LINUX_DISTRO_ID] [--boot_disk_image BOOT_DISK_IMAGE]
                                  [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --boot_disk_image_id BOOT_DISK_IMAGE_ID
                        Provide boot_disk_image_id to edit a specific boot disk image configuration.
  --boot_disk_image_name BOOT_DISK_IMAGE_NAME
                        Provide boot_disk_image_name to edit a specific boot disk image configuration.
  --name NAME           Provide name to edit a specific boot disk image configuration.
  --description DESCRIPTION
                        Provide description to edit a specific boot disk image configuration.
  --linux_distro_id LINUX_DISTRO_ID
                        Provide linux_distro_id to edit a specific boot disk image configuration.
  --boot_disk_image BOOT_DISK_IMAGE
                        Provide boot_disk_image to edit a specific boot disk image configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Provide true to edit output in YAML format. (default: false)
```

- edit-boot-disk-image-conf example with any one of the required argument '--boot_disk_image_id' and other optional argument is passed which is to be updated.

```bash
yeedu resource edit-boot-disk-image-conf --boot_disk_image_id=1 --description="dev boot disk"
```

- Console output

```bash
{
  "boot_disk_image_id": "1",
  "boot_disk_image_name": "yeedu_boot_disk_image",
  "description": "dev boot disk",
  "cloud_provider_id": 0,
  "linux_distro_id": 0,
  "boot_disk_image": "ubuntu-os-cloud/ubuntu-2004-lts",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-01-05T10:22:54.395Z",
  "from_date": "2024-01-05T10:09:27.590Z",
  "to_date": null
}
```

### delete-boot-disk-image-conf

```bash
yeedu resource delete-boot-disk-image-conf -h
```

```bash
usage:  delete-boot-disk-image-conf [-h] [--boot_disk_image_id BOOT_DISK_IMAGE_ID] [--boot_disk_image_name BOOT_DISK_IMAGE_NAME]
                                    [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --boot_disk_image_id BOOT_DISK_IMAGE_ID
                        Provide boot_disk_image_id to delete a specific boot disk image configuration.
  --boot_disk_image_name BOOT_DISK_IMAGE_NAME
                        Provide boot_disk_image_name to delete a specific boot disk image configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Provide true to delete output in YAML format. (default: false)
```

- delete-boot-disk-image-conf example with any one of the required argument '--boot_disk_image_id' is passed which is to be deleted.

```bash
yeedu resource delete-boot-disk-image-conf --boot_disk_image_id=1
```

- Console output

```bash
{
  "message": "Deleted boot disk image configuration id: 1."
}
```

## Credentials Configuration

| Command Name                                        | Utility                                                           |
| --------------------------------------------------- | ----------------------------------------------------------------- |
| [create-credential-conf](#create-credential-conf)   | To create a Credential Configuration.                             |
| [list-credential-confs](#list-credential-confs)     | To list all the available Credential Configurations.              |
| [search-credential-confs](#search-credential-confs) | To search all the Credential Configurations based on name.        |
| [get-credential-conf](#get-credential-conf)         | To get the information about a specific Credential Configuration. |
| [edit-credential-conf](#edit-credential-conf)       | To edit a specific Credential Configuration.                      |
| [delete-credential-conf](#delete-credential-conf)   | To delete a specific Credential Configuration.                    |

### create-credential-conf

```bash
yeedu resource create-credential-conf -h
```

```bash
usage:  create-credential-conf [-h] --name NAME --credential_type_id CREDENTIAL_TYPE_ID
                               --base64_encoded_credentials BASE64_ENCODED_CREDENTIALS
                               [--json-output [{pretty,default}]]
                               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name NAME           Provide name to create-credential-conf.
  --description DESCRIPTION
                        Provide description to create-credential-conf.
  --credential_type_id CREDENTIAL_TYPE_ID
                        Provide credential_type_id to create-credential-conf.
  --base64_encoded_credentials BASE64_ENCODED_CREDENTIALS
                        Provide base64_encoded_credentials to create-credential-conf.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-credential-conf example with all the required arguments passed.

```bash
yeedu resource create-credential-conf  --name='yeedu-svc' --credential_type_id=0 --base64_encoded_credentials='ew0KICAieWVlZHVfY3JlZGVudGlhbHMiOiAiRHVtbXkgQ3JlZGVudGlhbHMgQ29uZmlndXJhdGlvbiINCn0'
```

- Console output

```bash
{
  "credentials_conf_id": "1",
  "name": "yeedu-svc",
  "description": null,
  "credential_type_id": "0",
  "tenant_id": "e67f00ad-68aa-46d0-b32e-f3f8dac5427d",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2023-09-28T17:28:11.325Z",
  "from_date": "2023-09-28T17:28:11.325Z",
  "to_date": null
}
```

### list-credential-confs

```bash
yeedu resource list-credential-confs -h
```

```bash
usage:  list-credential-confs [-h] [--cloud_provider [{GCP,AWS,Azure}]]
                              [--page_number PAGE_NUMBER] [--limit LIMIT]
                              [--json-output [{pretty,default}]]
                              [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider [{GCP,AWS,Azure}]
                        Cloud Provider that will be used for filtering Credential
                        Configurations.
  --page_number PAGE_NUMBER
                        To list Credential Configurations for a specific page_number.
                        (default: 1)
  --limit LIMIT         Provide limit to list number of Credential Configurations.
                        (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-credential-confs example with optional arguments passed.

```bash
yeedu resource list-credential-confs --cloud_provider="GCP"
```

- Console output

```bash
{
  "data": [
    {
      "credentials_conf_id": 1,
      "credentials_conf_name": "yeedu-svc",
      "description": null,
      "credential_type": {
        "credential_type_id": 0,
        "name": "Google Service Account",
        "cloud_provider": {
          "name": "GCP",
          "description": "Provider for creating infrastructure on Google Cloud Platform"
        }
      },
      "tenant_id": "e67f00ad-68aa-46d0-b32e-f3f8dac5427d",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-05-30T07:59:47.616616+00:00",
      "from_date": "2024-05-30T07:59:47.616616+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-credential-confs

```bash
yeedu resource search-credential-confs -h
```

```bash
usage:  search-credential-confs [-h] --credentials_conf_name CREDENTIALS_CONF_NAME
                                [--cloud_provider [{GCP,AWS,Azure}]]
                                [--page_number PAGE_NUMBER] [--limit LIMIT]
                                [--json-output [{pretty,default}]]
                                [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --credentials_conf_name CREDENTIALS_CONF_NAME
                        Provide credentials_conf_name to search credential
                        configuration.
  --cloud_provider [{GCP,AWS,Azure}]
                        Cloud Provider that will be used for filtering Credential
                        Configurations.
  --page_number PAGE_NUMBER
                        To search Credential Configurations for a specific page_number.
                        (default: 1)
  --limit LIMIT         Provide limit to search number of Credential Configurations.
                        (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-credential-confs example with required argument '--credentials_conf_name' passed.

```bash
yeedu resource search-credential-confs --credentials_conf_name="yeedu"
```

- Console output

```bash
{
  "data": [
    {
      "credentials_conf_id": 1,
      "credentials_conf_name": "yeedu-svc",
      "description": null,
      "credential_type": {
        "credential_type_id": 0,
        "name": "Google Service Account",
        "cloud_provider": {
          "name": "GCP",
          "description": "Provider for creating infrastructure on Google Cloud Platform"
        }
      },
      "tenant_id": "e67f00ad-68aa-46d0-b32e-f3f8dac5427d",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-05-30T07:59:47.616616+00:00",
      "from_date": "2024-05-30T07:59:47.616616+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-credential-conf

```bash
yeedu resource get-credential-conf -h
```

```bash
usage:  get-credential-conf [-h] [--credentials_conf_id CREDENTIALS_CONF_ID]
                            [--credentials_conf_name CREDENTIALS_CONF_NAME]
                            [--json-output [{pretty,default}]]
                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --credentials_conf_id CREDENTIALS_CONF_ID
                        Provide credentials_conf_id to get information about a specific
                        credential configuration.
  --credentials_conf_name CREDENTIALS_CONF_NAME
                        Provide credentials_conf_name to get information about a
                        specific credential configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-credential-conf example with any one of the required '--credentials_conf_name' arguments passed.

```bash
yeedu resource get-credential-conf --credentials_conf_name=""
```

- Console output

```bash
{
  "credentials_conf_id": 1,
  "credentials_conf_name": "yeedu-svc",
  "description": null,
  "credential_type": {
    "credential_type_id": 0,
    "name": "Google Service Account",
    "cloud_provider": {
      "name": "GCP",
      "description": "Provider for creating infrastructure on Google Cloud Platform"
    }
  },
  "tenant_id": "e67f00ad-68aa-46d0-b32e-f3f8dac5427d",
  "created_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "last_update_date": "2024-05-30T07:59:47.616616+00:00",
  "from_date": "2024-05-30T07:59:47.616616+00:00",
  "to_date": "infinity"
}
```

### edit-credential-conf

```bash
yeedu resource edit-credential-conf -h
```

```bash
usage:  edit-credential-conf [-h] [--credentials_conf_id CREDENTIALS_CONF_ID]
                             [--credentials_conf_name CREDENTIALS_CONF_NAME]
                             [--name NAME]
                             [--base64_encoded_credentials BASE64_ENCODED_CREDENTIALS]
                             [--json-output [{pretty,default}]]
                             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --credentials_conf_id CREDENTIALS_CONF_ID
                        Provide credentials_conf_id to edit a specific Credential Configuration.
  --credentials_conf_name CREDENTIALS_CONF_NAME
                        Provide credentials_conf_name to edit a specific Credential Configuration.
  --name NAME           Provide name to edit-credential-conf.
  --description DESCRIPTION
                        Provide description to edit-credential-conf.
  --base64_encoded_credentials BASE64_ENCODED_CREDENTIALS
                        Provide base64_encoded_credentials to edit-credential-conf.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- edit-credential-conf example with any one of the required '--credentials_conf_id' argument and other optional argument is passed which is to be updated.

```bash
yeedu resource edit-credential-conf --credentials_conf_id=1 --name='yeedu-svc'
```

- Console output

```bash
{
  "credentials_conf_id": "1",
  "name": "yeedu-svc",
  "credential_type_id": "0",
  "tenant_id": "e67f00ad-68aa-46d0-b32e-f3f8dac5427d",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2023-09-28T17:33:36.788Z",
  "from_date": "2023-09-28T17:28:11.325Z",
  "to_date": null
}
```

### delete-credential-conf

```bash
yeedu resource delete-credential-conf -h
```

```bash
usage:  delete-credential-conf [-h] [--credentials_conf_id CREDENTIALS_CONF_ID]
                               [--credentials_conf_name CREDENTIALS_CONF_NAME]
                               [--json-output [{pretty,default}]]
                               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --credentials_conf_id CREDENTIALS_CONF_ID
                        Provide credentials_conf_id to delete a specific Credential
                        Configuration.
  --credentials_conf_name CREDENTIALS_CONF_NAME
                        Provide credentials_conf_name to delete a specific Credential
                        Configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- delete-credential-conf example with any one of the required '--credentials_conf_name' argument passed.

```bash
yeedu resource delete-credential-conf --credentials_conf_name="yeedu-svc"
```

- Console output

```bash
{
  "message": "Deleted Credentials Configuration Name: 'yeedu-svc'."
}
```

## Cloud Env

| Command Name                            | Utility                                                          |
| --------------------------------------- | ---------------------------------------------------------------- |
| [create-cloud-env](#create-cloud-env)   | To create a Object Storage Manager.                              |
| [list-cloud-envs](#list-cloud-envs)     | To list all the available Object Storage Manager Configurations. |
| [search-cloud-envs](#search-cloud-envs) | To search Object Storage Manager Configurations.                 |
| [get-cloud-env](#get-cloud-env)         | To get information about a specific Object Storage Manager.      |
| [edit-cloud-env](#edit-cloud-env)       | To edit a specific Object Storage Manager Configuration.         |
| [delete-cloud-env](#delete-cloud-env)   | To delete a specific Object Storage Manager.                     |

### create-cloud-env

```bash
yeedu resource create-cloud-env -h
```

```bash
usage:  create-cloud-env [-h] --name NAME [--description DESCRIPTION]
                         --cloud_provider_id CLOUD_PROVIDER_ID
                         --availability_zone_id AVAILABILITY_ZONE_ID
                         --network_conf_id NETWORK_CONF_ID
                         --cloud_project CLOUD_PROJECT
                         --credential_config_id CREDENTIAL_CONFIG_ID
                         --boot_disk_image_id BOOT_DISK_IMAGE_ID
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name NAME           Provide name to create a cloud environment.
  --description DESCRIPTION
                        Provide description to create a cloud environment.
  --cloud_provider_id CLOUD_PROVIDER_ID
                        Provide cloud_provider_id to create a cloud environment.
  --availability_zone_id AVAILABILITY_ZONE_ID
                        Provide availability_zone_id to create a cloud environment.
  --network_conf_id NETWORK_CONF_ID
                        Provide network_conf_id to create a cloud environment.
  --cloud_project CLOUD_PROJECT
                        Provide cloud_project to create a cloud environment.
  --credential_config_id CREDENTIAL_CONFIG_ID
                        Provide credential_config_id to create a cloud environment.
  --boot_disk_image_id BOOT_DISK_IMAGE_ID
                        Provide boot_disk_image_id to create a cloud environment.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-cloud-env example with all the required arguments passed.

```bash
yeedu resource create-cloud-env --name="gcp_cloud_env" --cloud_provider_id=0 --availability_zone_id=75 --network_conf_id=1 --cloud_project="yeedu" --credential_config_id=1 --boot_disk_image_id=1
```

- Console output

```bash
{
  "cloud_env_id": "1",
  "name": "gcp_cloud_env",
  "description": null,
  "cloud_provider_id": "0",
  "availability_zone_id": "75",
  "network_conf_id": "1",
  "cloud_project": "yeedu",
  "credential_config_id": "1",
  "boot_disk_image_id": "1",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-01-08T09:07:25.748Z",
  "from_date": "2024-01-08T09:07:25.748Z",
  "to_date": null
}
```

### list-cloud-envs

```bash
yeedu resource list-cloud-envs -h
```

```bash
usage:  list-cloud-envs [-h] [--cloud_provider [{GCP,AWS,Azure}]]
                        [--page_number PAGE_NUMBER] [--limit LIMIT]
                        [--json-output [{pretty,default}]]
                        [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider [{GCP,AWS,Azure}]
                        Provide cloud_provider to list all the related cloud environments of a specific cloud provider.
  --page_number PAGE_NUMBER
                        To list cloud environments for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of cloud environments. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-cloud-envs example with an optional argument passed.

```bash
yeedu resource list-cloud-envs --cloud_provider="GCP"
```

- Console output

```bash
{
  "data": [
    {
      "cloud_env_id": 1,
      "cloud_env_name": "gcp_cloud_env",
      "description": "yeedu cloud environment",
      "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP",
        "description": "Provider for creating infrastructure on Google Cloud Platform"
      },
      "availability_zone": {
        "availability_zone_id": 75,
        "name": "us-central1-a",
        "cloud_provider_id": 0,
        "region": "us-central1",
        "description": "Council Bluffs, Iowa, North America"
      },
      "network_config": {
        "network_conf_id": 1,
        "network_conf_name": "yeedu_gcp_network",
        "description": null,
        "network_project_id": "yeedu",
        "network_name": "yeedu-vpc",
        "network_tags": [
          "yeedu"
        ],
        "subnet": "custom-subnet-yeedu",
        "availability_zone": {
          "availability_zone_id": 75,
          "name": "us-central1-a",
          "cloud_provider_id": 0,
          "region": "us-central1",
          "description": "Council Bluffs, Iowa, North America"
        }
      },
      "cloud_project": "yeedu",
      "credential_config": {
        "credential_conf_id": 1,
        "credentials_conf_name": "yeedu-svc",
        "description": null,
        "credential_type": {
          "credential_type_id": 0,
          "name": "Google Service Account",
          "cloud_provider_id": 0
        }
      },
      "boot_disk_image": {
        "boot_disk_image_id": 1,
        "boot_disk_image_name": "gcp_boot_disk",
        "description": "dev boot disk",
        "linux_distro": {
          "linux_distro_id": 0,
          "distro_name": "UBUNTU",
          "distro_version": "20.04 LTS"
        },
        "boot_disk_image": "ubuntu-os-cloud/ubuntu-2004-lts"
      },
      "tenant_id": "1ea17e91-257b-4a6c-82aa-265568d31615",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-05-30T08:00:41.996333+00:00",
      "from_date": "2024-05-30T08:00:41.996333+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-cloud-envs

```bash
yeedu resource search-cloud-envs -h
```

```bash
usage:  search-cloud-envs [-h] --cloud_env_name CLOUD_ENV_NAME
                          [--cloud_provider [{GCP,AWS,Azure}]]
                          [--page_number PAGE_NUMBER] [--limit LIMIT]
                          [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_env_name CLOUD_ENV_NAME
                        Provide cloud_env_name to search matching cloud environments.
  --cloud_provider [{GCP,AWS,Azure}]
                        Provide cloud_provider to search all the related cloud environments of a specific cloud provider.
  --page_number PAGE_NUMBER
                        To list cloud environments for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of cloud environments. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-cloud-envs example with required argument '--cloud_env_name' passed.

```bash
yeedu resource search-cloud-envs --cloud_env_name="gcp_"
```

- Console output

```bash
{
  "data": [
    {
      "cloud_env_id": 1,
      "cloud_env_name": "gcp_cloud_env",
      "description": "yeedu cloud environment",
      "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP",
        "description": "Provider for creating infrastructure on Google Cloud Platform"
      },
      "availability_zone": {
        "availability_zone_id": 75,
        "name": "us-central1-a",
        "cloud_provider_id": 0,
        "region": "us-central1",
        "description": "Council Bluffs, Iowa, North America"
      },
      "network_config": {
        "network_conf_id": 1,
        "network_conf_name": "yeedu_gcp_network",
        "description": null,
        "network_project_id": "yeedu",
        "network_name": "yeedu-vpc",
        "network_tags": [
          "yeedu"
        ],
        "subnet": "custom-subnet-yeedu",
        "availability_zone": {
          "availability_zone_id": 75,
          "name": "us-central1-a",
          "cloud_provider_id": 0,
          "region": "us-central1",
          "description": "Council Bluffs, Iowa, North America"
        }
      },
      "cloud_project": "yeedu",
      "credential_config": {
        "credential_conf_id": 1,
        "credentials_conf_name": "yeedu-svc",
        "description": null,
        "credential_type": {
          "credential_type_id": 0,
          "name": "Google Service Account",
          "cloud_provider_id": 0
        }
      },
      "boot_disk_image": {
        "boot_disk_image_id": 1,
        "boot_disk_image_name": "gcp_boot_disk",
        "description": "dev boot disk",
        "linux_distro": {
          "linux_distro_id": 0,
          "distro_name": "UBUNTU",
          "distro_version": "20.04 LTS"
        },
        "boot_disk_image": "ubuntu-os-cloud/ubuntu-2004-lts"
      },
      "tenant_id": "1ea17e91-257b-4a6c-82aa-265568d31615",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-05-30T08:00:41.996333+00:00",
      "from_date": "2024-05-30T08:00:41.996333+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-cloud-env

```bash
yeedu resource get-cloud-env -h
```

```bash
usage:  get-cloud-env [-h] [--cloud_env_id CLOUD_ENV_ID]
                      [--cloud_env_name CLOUD_ENV_NAME]
                      [--json-output [{pretty,default}]]
                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_env_id CLOUD_ENV_ID
                        Provide cloud_env_id to get detials about a specific cloud environment.
  --cloud_env_name CLOUD_ENV_NAME
                        Provide cloud_env_name to get detials about a specific cloud environment.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-cloud-env example with any one of the required argument passed.

```bash
yeedu resource get-cloud-env --cloud_env_id=1
```

- Console output

```bash
{
  "cloud_env_id": 1,
  "cloud_env_name": "gcp_cloud_env",
  "description": "yeedu cloud environment",
  "cloud_provider": {
    "cloud_provider_id": 0,
    "name": "GCP",
    "description": "Provider for creating infrastructure on Google Cloud Platform"
  },
  "availability_zone": {
    "availability_zone_id": 75,
    "name": "us-central1-a",
    "cloud_provider_id": 0,
    "region": "us-central1",
    "description": "Council Bluffs, Iowa, North America"
  },
  "network_config": {
    "network_conf_id": 1,
    "network_conf_name": "yeedu_gcp_network",
    "description": null,
    "network_project_id": "yeedu",
    "network_name": "yeedu-vpc",
    "network_tags": [
      "yeedu"
    ],
    "subnet": "custom-subnet-yeedu",
    "availability_zone": {
      "availability_zone_id": 75,
      "name": "us-central1-a",
      "cloud_provider_id": 0,
      "region": "us-central1",
      "description": "Council Bluffs, Iowa, North America"
    }
  },
  "cloud_project": "yeedu",
  "credential_config": {
    "credential_conf_id": 1,
    "credentials_conf_name": "yeedu-svc",
    "description": null,
    "credential_type": {
      "credential_type_id": 0,
      "name": "Google Service Account",
      "cloud_provider_id": 0
    }
  },
  "boot_disk_image": {
    "boot_disk_image_id": 1,
    "boot_disk_image_name": "gcp_boot_disk",
    "description": "dev boot disk",
    "linux_distro": {
      "linux_distro_id": 0,
      "distro_name": "UBUNTU",
      "distro_version": "20.04 LTS"
    },
    "boot_disk_image": "ubuntu-os-cloud/ubuntu-2004-lts"
  },
  "tenant_id": "1ea17e91-257b-4a6c-82aa-265568d31615",
  "created_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "last_update_date": "2024-05-30T08:00:41.996333+00:00",
  "from_date": "2024-05-30T08:00:41.996333+00:00",
  "to_date": "infinity"
}
```

### edit-cloud-env

```bash
yeedu resource edit-cloud-env -h
```

```bash
usage:  edit-cloud-env [-h] [--cloud_env_id CLOUD_ENV_ID]
                       [--cloud_env_name CLOUD_ENV_NAME] [--name NAME]
                       [--description DESCRIPTION]
                       [--availability_zone_id AVAILABILITY_ZONE_ID]
                       [--network_conf_id NETWORK_CONF_ID]
                       [--cloud_project CLOUD_PROJECT]
                       [--credential_config_id CREDENTIAL_CONFIG_ID]
                       [--boot_disk_image_id BOOT_DISK_IMAGE_ID]
                       [--json-output [{pretty,default}]]
                       [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_env_id CLOUD_ENV_ID
                        Provide cloud_env_id to edit a specific cloud environment.
  --cloud_env_name CLOUD_ENV_NAME
                        Provide cloud_env_name to edit a specific cloud environment.
  --name NAME           Provide name to edit a specific cloud environment.
  --description DESCRIPTION
                        Provide description to edit a specific cloud environment.
  --availability_zone_id AVAILABILITY_ZONE_ID
                        Provide availability_zone_id to edit a specific cloud environment.
  --network_conf_id NETWORK_CONF_ID
                        Provide network_conf_id to edit a specific cloud environment.
  --cloud_project CLOUD_PROJECT
                        Provide cloud_project to edit a specific cloud environment.
  --credential_config_id CREDENTIAL_CONFIG_ID
                        Provide credential_config_id to edit a specific cloud environment.
  --boot_disk_image_id BOOT_DISK_IMAGE_ID
                        Provide boot_disk_image_id to edit a specific cloud environment.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Provide true to edit output in YAML format. (default: false)
```

- edit-cloud-env example with all the required arguments passed which needs to be updated.

```bash
yeedu resource edit-cloud-env --cloud_env_id=1 --name="gcp_cloud_env_dev"
```

- Console output

```bash
{
  "cloud_env_id": "1",
  "name": "gcp_cloud_env_dev",
  "description": null,
  "cloud_provider_id": "0",
  "availability_zone_id": "75",
  "network_conf_id": "1",
  "cloud_project": "yeedu",
  "credential_config_id": "1",
  "boot_disk_image_id": "1",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-01-08T09:07:25.748Z",
  "from_date": "2024-01-08T09:07:25.748Z",
  "to_date": null
}
```

### delete-cloud-env

```bash
yeedu resource delete-cloud-env -h
```

```bash
usage:  delete-cloud-env [-h] [--cloud_env_id CLOUD_ENV_ID]
                         [--cloud_env_name CLOUD_ENV_NAME]
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_env_id CLOUD_ENV_ID
                        Provide cloud_env_id to delete a specific cloud environment.
  --cloud_env_name CLOUD_ENV_NAME
                        Provide cloud_env_name to delete a specific cloud environment.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Provide true to delete output in YAML format. (default: false)
```

- delete-cloud-env example with any one of the required argument passed.

```bash
yeedu resource delete-cloud-env --cloud_env_id=1
```

- Console output

```bash
{
  "message": "Deleted cloud environment id: 1"
}
```

## Object Storage Manager

| Command Name                                                      | Utility                                                          |
| ----------------------------------------------------------------- | ---------------------------------------------------------------- |
| [create-object-storage-manager](#create-object-storage-manager)   | To create a Object Storage Manager.                              |
| [list-object-storage-managers](#list-object-storage-managers)     | To list all the available Object Storage Manager Configurations. |
| [search-object-storage-managers](#search-object-storage-managers) | To search Object Storage Manager Configurations.                 |
| [get-object-storage-manager](#get-object-storage-manager)         | To get information about a specific Object Storage Manager.      |
| [edit-object-storage-manager](#edit-object-storage-manager)       | To edit a specific Object Storage Manager Configuration.         |
| [delete-object-storage-manager](#delete-object-storage-manager)   | To delete a specific Object Storage Manager.                     |

### create-object-storage-manager

```bash
yeedu resource create-object-storage-manager -h
```

```bash
usage:  create-object-storage-manager [-h] --name NAME [--description DESCRIPTION] --cloud_provider_id CLOUD_PROVIDER_ID --credentials_conf_id
                                      CREDENTIALS_CONF_ID --object_storage_bucket_name OBJECT_STORAGE_BUCKET_NAME
                                      [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name NAME           Provide name to create-object-storage-manager.
  --description DESCRIPTION
                        Provide description to create-object-storage-manager.
  --cloud_provider_id CLOUD_PROVIDER_ID
                        Provide cloud_provider_id to create-object-storage-manager.
  --credentials_conf_id CREDENTIALS_CONF_ID
                        Provide credentials_conf_id to create-object-storage-manager.
  --object_storage_bucket_name OBJECT_STORAGE_BUCKET_NAME
                        Provide object_storage_bucket_name to create-object-storage-manager.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-object-storage-manager example with all the required arguments passed.

```bash
yeedu resource create-object-storage-manager --name="yeedu_osm" --cloud_provider_id=0 --credentials_conf_id=1 --object_storage_bucket_name="yeedu"
```

- Console output

```bash
{
  "object_storage_manager_id": "1",
  "name": "yeedu_object_storage_manager",
  "description": null,
  "cloud_provider_id": "0",
  "credentials_conf_id": "1",
  "object_storage_bucket_name": "yeedu",
  "tenant_id": "1ea17e91-257b-4a6c-82aa-265568d31615",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-01-08T09:32:24.643Z",
  "from_date": "2024-01-08T09:32:24.643Z",
  "to_date": null
}
```

### list-object-storage-managers

```bash
yeedu resource list-object-storage-managers -h
```

```bash
usage:  list-object-storage-managers [-h] [--cloud_provider [{GCP,AWS,Azure}]]
                                     [--page_number PAGE_NUMBER] [--limit LIMIT]
                                     [--json-output [{pretty,default}]]
                                     [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider [{GCP,AWS,Azure}]
                        Cloud Provider that will be used for filtering list.
  --page_number PAGE_NUMBER
                        To list Object Storage Managers for a specific page_number.
                        (default: 1)
  --limit LIMIT         Provide limit to list number of Object Storage Managers.
                        (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-object-storage-managers example with an optional argument passed.

```bash
yeedu resource list-object-storage-managers --cloud_provider="GCP"
```

- Console output

```bash
{
  "data": [
    {
      "object_storage_manager_id": 1,
      "object_storage_manager_name": "yeedu_object_storage_manager",
      "description": null,
      "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP",
        "description": "Provider for creating infrastructure on Google Cloud Platform"
      },
      "object_storage_bucket_name": "yeedu",
      "credentials_config": {
        "credentials_conf_id": 1,
        "credentials_conf_name": "gcp_credential",
        "description": null,
        "credential_type": {
          "credential_type_id": 0,
          "name": "Google Service Account"
        }
      },
      "tenant_id": "1ea17e91-257b-4a6c-82aa-265568d31615",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-05-30T08:07:10.727231+00:00",
      "from_date": "2024-05-30T08:07:10.727231+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-object-storage-managers

```bash
yeedu resource search-object-storage-managers -h
```

```bash
usage:  search-object-storage-managers [-h]
                                       --object_storage_manager_name
                                       OBJECT_STORAGE_MANAGER_NAME
                                       [--cloud_provider [{GCP,AWS,Azure}]]
                                       [--page_number PAGE_NUMBER]
                                       [--limit LIMIT]
                                       [--json-output [{pretty,default}]]
                                       [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME
                        Provide Object Storage Manager Name to search information about a specific Object Storage Manager.
  --cloud_provider [{GCP,AWS,Azure}]
                        Cloud Provider that will be used for filtering list.
  --page_number PAGE_NUMBER
                        To search Object Storage Managers for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of Object Storage Managers. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-object-storage-managers example with required argument '--object_storage_manager_name' passed.

```bash
yeedu resource search-object-storage-managers --object_storage_manager_name="gcp_"
```

- Console output

```bash
{
  "data": [
    {
      "object_storage_manager_id": 1,
      "object_storage_manager_name": "yeedu_object_storage_manager",
      "description": null,
      "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP",
        "description": "Provider for creating infrastructure on Google Cloud Platform"
      },
      "object_storage_bucket_name": "yeedu",
      "credentials_config": {
        "credentials_conf_id": 1,
        "credentials_conf_name": "gcp_credential",
        "description": null,
        "credential_type": {
          "credential_type_id": 0,
          "name": "Google Service Account"
        }
      },
      "tenant_id": "1ea17e91-257b-4a6c-82aa-265568d31615",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-05-30T08:07:10.727231+00:00",
      "from_date": "2024-05-30T08:07:10.727231+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-object-storage-manager

```bash
yeedu resource get-object-storage-manager -h
```

```bash
usage:  get-object-storage-manager [-h]
                                   [--object_storage_manager_id OBJECT_STORAGE_MANAGER_ID]
                                   [--object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME]
                                   [--json-output [{pretty,default}]]
                                   [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --object_storage_manager_id OBJECT_STORAGE_MANAGER_ID
                        Provide Object Storage Manager Id to get information about a specific Object Storage Manager.
  --object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME
                        Provide Object Storage Manager Name to get information about a specific Object Storage Manager.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-object-storage-manager example with any one of the required argument passed.

```bash
yeedu resource get-object-storage-manager --object_storage_manager_id=1
```

- Console output

```bash
{
  "object_storage_manager_id": 1,
  "object_storage_manager_name": "yeedu_object_storage_manager",
  "description": null,
  "cloud_provider": {
    "cloud_provider_id": 0,
    "name": "GCP",
    "description": "Provider for creating infrastructure on Google Cloud Platform"
  },
  "object_storage_bucket_name": "yeedu",
  "credentials_config": {
    "credentials_conf_id": 1,
    "credentials_conf_name": "gcp_credential",
    "description": null,
    "credential_type": {
      "credential_type_id": 0,
      "name": "Google Service Account"
    }
  },
  "tenant_id": "1ea17e91-257b-4a6c-82aa-265568d31615",
  "created_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "last_update_date": "2024-05-30T08:07:10.727231+00:00",
  "from_date": "2024-05-30T08:07:10.727231+00:00",
  "to_date": "infinity"
}
```

### edit-object-storage-manager

```bash
yeedu resource edit-object-storage-manager -h
```

```bash
usage:  edit-object-storage-manager [-h] [--object_storage_manager_id OBJECT_STORAGE_MANAGER_ID]
                                    [--object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME] [--name NAME] [--description DESCRIPTION]
                                    [--credentials_conf_id CREDENTIALS_CONF_ID] [--json-output [{pretty,default}]]
                                    [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --object_storage_manager_id OBJECT_STORAGE_MANAGER_ID
                        Provide object_storage_manager_id to edit information about a specific Object Storage Manager.
  --object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME
                        Provide object_storage_manager_name to edit information about a specific Object Storage Manager.
  --name NAME           Provide name to edit-object-storage-manager.
  --description DESCRIPTION
                        Provide description to edit-object-storage-manager.
  --credentials_conf_id CREDENTIALS_CONF_ID
                        Provide credentials_conf_id to edit-object-storage-manager.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- edit-object-storage-manager example with all the required arguments passed which needs to be updated.

```bash
yeedu resource edit-object-storage-manager --object_storage_manager_id=1 --name="yeedu_object_storage_manager"
```

- Console output

```bash
{
  "object_storage_manager_id": "1",
  "name": "yeedu_object_storage_manager",
  "description": null,
  "cloud_provider_id": "0",
  "credentials_conf_id": "1",
  "object_storage_bucket_name": "yeedu",
  "tenant_id": "1ea17e91-257b-4a6c-82aa-265568d31615",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-01-08T09:32:24.643Z",
  "from_date": "2024-01-08T09:32:24.643Z",
  "to_date": null
}
```

### delete-object-storage-manager

```bash
yeedu resource delete-object-storage-manager -h
```

```bash
usage:  delete-object-storage-manager [-h] [--object_storage_manager_id OBJECT_STORAGE_MANAGER_ID]
                                      [--object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME] [--json-output [{pretty,default}]]
                                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --object_storage_manager_id OBJECT_STORAGE_MANAGER_ID
                        Provide object_storage_manager_id to delete a specific Object Storage Manager.
  --object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME
                        Provide object_storage_manager_name to delete a specific Object Storage Manager.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- delete-object-storage-manager example with any one of the required argument passed.
 
```bash
yeedu resource delete-object-storage-manager --object_storage_manager_name="yeedu_object_storage_manager"
```

- Console output

```bash
{
  "message": "Deleted Object Storage Manager Configuration Name: 'yeedu_object_storage_manager'."
}
```

## Object Storage Manager Files

| Command Name                                                                | Utility                                                          |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [create-object-storage-manager-file](#create-object-storage-manager-file)   | To create a Object Storage Manager Files.                        |
| [list-object-storage-manager-files](#list-object-storage-manager-files)     | To list all the available Object Storage Manager Files.          |
| [search-object-storage-manager-files](#search-object-storage-manager-files) | To search all the available Object Storage Manager Files.        |
| [get-object-storage-manager-file](#get-object-storage-manager-file)         | To get information about a specific Object Storage Manager File. |
| [delete-object-storage-manager-file](#delete-object-storage-manager-file)   | To delete a specific Object Storage Manager File.                |

### create-object-storage-manager-file

```bash
yeedu resource create-object-storage-manager-file -h
```

```bash
usage:  create-object-storage-manager-file [-h]
                                           [--object_storage_manager_id OBJECT_STORAGE_MANAGER_ID]
                                           [--object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME]
                                           --local_file_path
                                           LOCAL_FILE_PATH
                                           [--overwrite [{true,false}]]
                                           [--recursive [{true,false}]]
                                           [--root_output_dir [ROOT_OUTPUT_DIR]]
                                           [--json-output [{pretty,default}]]
                                           [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --object_storage_manager_id OBJECT_STORAGE_MANAGER_ID
                        Provide Object Storage Manager Id to create-
                        object-storage-manager-file.
  --object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME
                        Provide Object Storage Manager Name to to create-
                        object-storage-manager-file.
  --local_file_path LOCAL_FILE_PATH
                        Provide local_file_path to create-object-storage-
                        manager-file.
  --overwrite [{true,false}]
                        Provide overwrite to create-object-storage-
                        manager-file. (default: false)
  --recursive [{true,false}]
                        Provide recursive to create-object-storage-
                        manager-file. (default: false)
  --root_output_dir [ROOT_OUTPUT_DIR]
                        Provide root_output_dir to create-object-storage-
                        manager-file.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to
                        'true'. (default: false)
```

- create-object-storage-manager-file example with all the required arguments passed.

```bash
yeedu resource create-object-storage-manager-file --object_storage_manager_id 159 --local_file_path ~/script_warm_start --root_output_dir /home/test
```

- Console output

```bash
{
  "object_storage_manager_file_id": "258",
  "object_storage_manager_id": "159",
  "file_name": "script_warm_start",
  "full_file_path": "file:///yeedu/object-storage-manager/home/test/script_warm_start",
  "file_size_bytes": "503",
  "file_type": "",
  "is_dir": false,
  "parent_id": "257",
  "tenant_id": "8cee6100-7086-4138-92fd-712046174e91",
  "created_by_user_id": "32",
  "modified_by_user_id": "32",
  "last_update_date": "2025-01-13T13:58:58.514Z",
  "from_date": "2025-01-13T13:58:58.514Z",
  "to_date": null
}
```

### list-object-storage-manager-files

```bash
yeedu resource list-object-storage-manager-files -h
```

```bash
usage:  list-object-storage-manager-files [-h]
                                          [--object_storage_manager_id OBJECT_STORAGE_MANAGER_ID]
                                          [--object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME]
                                          [--file_id FILE_ID]
                                          [--file_path FILE_PATH]
                                          [--recursive [{true,false}]]
                                          [--page_number PAGE_NUMBER]
                                          [--limit LIMIT]
                                          [--json-output [{pretty,default}]]
                                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --object_storage_manager_id OBJECT_STORAGE_MANAGER_ID
                        Provide Object Storage Manager Id to list all the
                        available Object Storage Manager Files.
  --object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME
                        Provide Object Storage Manager Name to list all
                        the available Object Storage Manager Files.
  --file_id FILE_ID     Provide Object Storage Manager File Id to list all
                        the available Files.
  --file_path FILE_PATH
                        Provide Object Storage Manager File Path to list
                        all the available Files.
  --recursive [{true,false}]
                        Provide recursive to list files recursively.
                        (default: false)
  --page_number PAGE_NUMBER
                        To list Object Storage Manager Files for a
                        specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of Object Storage
                        Manager Files. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to
                        'true'. (default: false)
```

- list-object-storage-manager-files example with any one of the required argument passed.

```bash
yeedu resource list-object-storage-manager-files --object_storage_manager_id 159 --limit 1
"
```

- Console output

```bash
{
  "data": [
    {
      "object_storage_manager_file_id": 129,
      "object_storage_manager": {
        "object_storage_manager_id": 159,
        "object_storage_manager_name": "test_osm",
        "description": null,
        "cloud_provider": {
          "name": "GCP",
          "description": "Provider for creating infrastructure on Google Cloud Platform"
        },
        "credentials_config": {
          "credential_config_id": 187,
          "name": "gcp_credential_diagnostics_informatics",
          "description": "test",
          "credential_type": {
            "credential_type_id": 0,
            "name": "Google Service Account"
          }
        },
        "object_storage_bucket_name": "yeedu-qa"
      },
      "file_name": "ui_team_workspace.yeedu",
      "full_file_path": "file:///yeedu/object-storage-manager/ui_team_workspace.yeedu",
      "file_size_bytes": "10634029",
      "file_type": "yeedu",
      "is_dir": false,
      "parent_id": null,
      "tenant_id": "8cee6100-7086-4138-92fd-712046174e91",
      "created_by": {
        "user_id": 2,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 2,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2024-12-20T04:21:15.383346+00:00",
      "from_date": "2024-12-20T04:21:15.383346+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 26,
    "total_pages": 26,
    "limit": 1,
    "next_page": 2
  }
}
```

### search-object-storage-manager-files

```bash
yeedu resource search-object-storage-manager-files -h
```

```bash
usage:  search-object-storage-manager-files [-h] --file_name FILE_NAME
                                            [--object_storage_manager_id OBJECT_STORAGE_MANAGER_ID]
                                            [--object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME]
                                            [--file_id FILE_ID]
                                            [--file_path FILE_PATH]
                                            [--recursive [{true,false}]]
                                            [--page_number PAGE_NUMBER]
                                            [--limit LIMIT]
                                            [--json-output [{pretty,default}]]
                                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --file_name FILE_NAME
                        Provide File Name to search all the available
                        Object Storage Manager Files.
  --object_storage_manager_id OBJECT_STORAGE_MANAGER_ID
                        Provide Object Storage Manager Id to search all
                        the available Object Storage Manager Files.
  --object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME
                        Provide Object Storage Manager Name to search all
                        the available Object Storage Manager Files.
  --file_id FILE_ID     Provide Object Storage Manager File Id to search
                        all the available Files.
  --file_path FILE_PATH
                        Provide Object Storage Manager File Path to search
                        all the available Files.
  --recursive [{true,false}]
                        Provide recursive to search files recursively.
                        (default: false)
  --page_number PAGE_NUMBER
                        To search Object Storage Manager Files for a
                        specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of Object Storage
                        Manager Files. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to
                        'true'. (default: false)
```

- search-object-storage-manager-files example with any one of the required argument passed.

```bash
yeedu resource search-object-storage-manager-files --file_name ui_team --object_storage_manager_id 159 --limit 1
```

- Console output

```bash
{
  "data": [
    {
      "object_storage_manager_file_id": 129,
      "object_storage_manager": {
        "object_storage_manager_id": 159,
        "object_storage_manager_name": "test_osm",
        "description": null,
        "cloud_provider": {
          "name": "GCP",
          "description": "Provider for creating infrastructure on Google Cloud Platform"
        },
        "credentials_config": {
          "credential_config_id": 187,
          "name": "gcp_credential_diagnostics_informatics",
          "description": "test",
          "credential_type": {
            "credential_type_id": 0,
            "name": "Google Service Account"
          }
        },
        "object_storage_bucket_name": "yeedu-qa"
      },
      "file_name": "ui_team_workspace.yeedu",
      "full_file_path": "file:///yeedu/object-storage-manager/ui_team_workspace.yeedu",
      "file_size_bytes": "10634029",
      "file_type": "yeedu",
      "is_dir": false,
      "parent_id": null,
      "tenant_id": "8cee6100-7086-4138-92fd-712046174e91",
      "created_by": {
        "user_id": 2,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 2,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2024-12-20T04:21:15.383346+00:00",
      "from_date": "2024-12-20T04:21:15.383346+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 1
  }
}
```

### get-object-storage-manager-file

```bash
yeedu resource get-object-storage-manager-file -h
```

```bash
usage:  get-object-storage-manager-file [-h] [--object_storage_manager_id OBJECT_STORAGE_MANAGER_ID]
                                        [--object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME] [--file_id FILE_ID]
                                        [--file_path FILE_PATH] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --object_storage_manager_id OBJECT_STORAGE_MANAGER_ID
                        Provide Object Storage Manager Id to get information
                        about a specific Object Storage Manager Files.
  --object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME
                        Provide Object Storage Manager Name to get
                        information about a specific Object Storage Manager
                        Files.
  --file_id FILE_ID     Provide File Id to get information about a specific
                        Object Storage Manager Files.
  --file_path FILE_PATH
                        Provide File Path to get information about a specific
                        Object Storage Manager Files.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to
                        'true'. (default: false)
```

- get-object-storage-manager-file example with any one of the required arguments passed.

```bash
yeedu resource get-object-storage-manager-file --object_storage_manager_id 159 --file_id 129
```

- Console output

```bash
{
  "object_storage_manager_file_id": 129,
  "object_storage_manager": {
    "object_storage_manager_id": 159,
    "object_storage_manager_name": "test_osm",
    "description": null,
    "cloud_provider": {
      "name": "GCP",
      "description": "Provider for creating infrastructure on Google Cloud Platform"
    },
    "credentials_config": {
      "credential_config_id": 187,
      "name": "gcp_credential_diagnostics_informatics",
      "description": "test",
      "credential_type": {
        "credential_type_id": 0,
        "name": "Google Service Account"
      }
    },
    "object_storage_bucket_name": "yeedu-qa"
  },
  "file_name": "ui_team_workspace.yeedu",
  "full_file_path": "file:///yeedu/object-storage-manager/ui_team_workspace.yeedu",
  "file_size_bytes": "10634029",
  "file_type": "yeedu",
  "is_dir": false,
  "parent_id": null,
  "tenant_id": "8cee6100-7086-4138-92fd-712046174e91",
  "created_by": {
    "user_id": 2,
    "username": "ysu0000@yeedu.io"
  },
  "modified_by": {
    "user_id": 2,
    "username": "ysu0000@yeedu.io"
  },
  "last_update_date": "2024-12-20T04:21:15.383346+00:00",
  "from_date": "2024-12-20T04:21:15.383346+00:00",
  "to_date": "infinity"
}
```

### delete-object-storage-manager-file

```bash
yeedu resource delete-object-storage-manager-file -h
```

```bash
usage:  delete-object-storage-manager-file [-h]
                                           [--object_storage_manager_id OBJECT_STORAGE_MANAGER_ID]
                                           [--object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME]
                                           [--file_id FILE_ID]
                                           [--file_path FILE_PATH]
                                           [--json-output [{pretty,default}]]
                                           [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --object_storage_manager_id OBJECT_STORAGE_MANAGER_ID
                        Provide Object Storage Manager Id to delete a
                        specific Object Storage Manager File.
  --object_storage_manager_name OBJECT_STORAGE_MANAGER_NAME
                        Provide Object Storage Manager Name to delete a
                        specific Object Storage Manager File.
  --file_id FILE_ID     Provide File Id to delete a specific Object Storage
                        Manager Files.
  --file_path FILE_PATH
                        Provide File Path to delete a specific Object Storage
                        Manager Files.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to
                        'true'. (default: false)
```

- delete-object-storage-manager-file example with any one of the required arguments passed.

```bash
 yeedu resource delete-object-storage-manager-file --object_storage_manager_id 159 --file_id 260
```

- Console output

```bash
{
  "message": "The File: 'yeedu/object-storage-manager/test/script_warm_start' has been deleted."
}
```

# Cluster

## Cluster Configuration

| Command Name                  | Utility                                                    |
| ----------------------------- | ---------------------------------------------------------- |
| [create-conf](#create-conf)   | Create a new cluster configuration.                        |
| [list-confs](#list-confs)     | List all the cluster configurations.                       |
| [search-confs](#search-confs) | Search cluster configurations based on configuration name. |
| [get-conf](#get-conf)         | Get details of a specific cluster configuration.           |
| [edit-conf](#edit-conf)       | Modify details of a specific cluster configuration.        |
| [delete-conf](#delete-conf)   | Delete a specific cluster configuration.                   |

### create-conf

```bash
yeedu cluster create-conf -h
```

```bash
usage:  create-conf [-h] --name NAME [--description DESCRIPTION]
                    --machine_type_category_id MACHINE_TYPE_CATEGORY_ID --machine_type_id
                    MACHINE_TYPE_ID [--volume_conf_id VOLUME_CONF_ID]
                    [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name NAME           Assigns a name to the cluster configuration.
  --description DESCRIPTION
                        Provides a description for the cluster configuration.
  --machine_type_category_id MACHINE_TYPE_CATEGORY_ID
                        Sets the machine type category ID for the cluster configuration.
  --machine_type_id MACHINE_TYPE_ID
                        Sets the machine type ID for the cluster configuration.
  --volume_conf_id VOLUME_CONF_ID
                        Sets the volume configuration ID for the cluster configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-conf example with all the required arguments passed.

```bash
yeedu cluster create-conf --name="yeedu_cluster_config" --description="Cluster Configurations test" --machine_type_id=1 --machine_type_category_id=2 --volume_conf_id=1
```

- Console output

```bash
{
  "cluster_conf_id": "242",
  "name": "yeedu_cluster_config",
  "description": "Cluster Configurations test",
  "machine_type_category_id": "2",
  "machine_type_id": "1",
  "volume_conf_id": "1",
  "created_by_user_id": "3",
  "modified_by_user_id": "3",
  "last_update_date": "2024-06-06T09:55:54.581Z",
  "from_date": "2024-06-06T09:55:54.581Z",
  "to_date": null
}
```

### list-confs

```bash
yeedu cluster list-confs -h
```

```bash
usage:  list-confs [-h] [--cloud_provider [{GCP,AWS,Azure}]]
                   [--compute_type [{compute_optimized,memory_optimized,general_purpose,gpu_accelerated}]]
                   [--page_number PAGE_NUMBER] [--limit LIMIT]
                   [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cloud_provider [{GCP,AWS,Azure}]
                        Specifies the cloud provider to filter the cluster
                        configurations.
  --compute_type [{compute_optimized,memory_optimized,general_purpose,gpu_accelerated}]
                        Specifies the compute type to filter the cluster configurations.
  --page_number PAGE_NUMBER
                        Specifies the page number for results pagination. (default: 1)
  --limit LIMIT         Specifies the maximum number of configurations to list per page.
                        (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-confs example with optional arguments passed.

```bash
yeedu cluster list-confs --cloud_provider="GCP" --limit=1
```

- Console output

```bash
{
  "data": [
    {
      "cluster_conf_id": 1,
      "cluster_conf_name": "n1-highcpu-16",
      "description": null,
      "machine_type_category": "compute_optimized",
      "machine_type": {
        "machine_type_id": 1,
        "cloud_provider": {
          "cloud_provider_id": 0,
          "name": "GCP"
        },
        "name": "n1-highcpu-16",
        "vCPUs": 16,
        "memory": "14.4 GiB",
        "has_cuda": false,
        "gpu_model": null,
        "gpus": 0,
        "gpu_memory": null,
        "cpu_model": [
          "Intel Xeon Scalable (Skylake) 1st Generation",
          "Intel Xeon E5 v4 (Broadwell E5)",
          "Intel Xeon E5 v3 (Haswell)",
          "Intel Xeon E5 v2 (Ivy Bridge)",
          "Intel Xeon E5 (Sandy Bridge)"
        ],
        "cpu_min_frequency_GHz": [
          "2.0",
          "2.2",
          "2.3",
          "2.5",
          "2.6"
        ],
        "cpu_max_frequency_GHz": [
          "3.5",
          "3.7",
          "3.8",
          "3.5",
          "3.6"
        ],
        "has_local_disk": false,
        "local_disk_size_GB": null,
        "local_num_of_disks": null,
        "local_disk_bus_type": {
          "local_disk_bus_type_id": null,
          "local_disk_bus_type": null
        },
        "local_disk_throughput_MB": null,
        "machine_price_ycu": 5.44
      },
      "machine_volume_conf": {
        "volume_conf_id": 3,
        "name": "volume_gcp_3",
        "encrypted": true,
        "size": 375,
        "disk_type": {
          "disk_type_id": 2,
          "cloud_provider": {
            "cloud_provider_id": 0,
            "name": "GCP"
          },
          "name": "local-ssd",
          "has_fixed_size": true,
          "min_size": 375,
          "max_size": 375
        },
        "machine_volume_num": 3,
        "machine_volume_strip_num": 3,
        "disk_iops": null,
        "disk_throughput_MB": null,
        "disk_num": 1,
        "disk_size": 1125
      },
      "created_by": null,
      "modified_by": null,
      "last_update_date": "2024-05-29T16:09:48.827146+00:00",
      "from_date": "2024-05-29T16:09:48.827146+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 49,
    "total_pages": 49,
    "limit": 1,
    "next_page": 2
  }
}
```

### search-confs

```bash
yeedu cluster search-confs -h
```

```bash
usage:  search-confs [-h] --cluster_conf_name CLUSTER_CONF_NAME
                     [--cloud_provider [{GCP,AWS,Azure}]]
                     [--compute_type {compute_optimized,memory_optimized,general_purpose,gpu_accelerated}]
                     [--page_number PAGE_NUMBER] [--limit LIMIT]
                     [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_conf_name CLUSTER_CONF_NAME
                        Specifies the name of the cluster configuration to search for.
  --cloud_provider [{GCP,AWS,Azure}]
                        Specifies the cloud provider to filter the cluster
                        configurations.
  --compute_type {compute_optimized,memory_optimized,general_purpose,gpu_accelerated}
                        Specifies the compute type to filter the cluster configurations.
  --page_number PAGE_NUMBER
                        Specifies the page number for results pagination. (default: 1)
  --limit LIMIT         Specifies the maximum number of configurations to search per
                        page. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-confs example with required argument '--cluster_conf_name' passed.

```bash
yeedu cluster search-confs --cluster_conf_name="yeedu_"
```

- Console output

```bash
{
  "data": [
    {
      "cluster_conf_id": 242,
      "cluster_conf_name": "yeedu_cluster_config",
      "description": "Cluster Configurations test",
      "machine_type_category": "general_purpose",
      "machine_type": {
        "machine_type_id": 1,
        "cloud_provider": {
          "cloud_provider_id": 0,
          "name": "GCP"
        },
        "name": "n1-highcpu-16",
        "vCPUs": 16,
        "memory": "14.4 GiB",
        "has_cuda": false,
        "gpu_model": null,
        "gpus": 0,
        "gpu_memory": null,
        "cpu_model": [
          "Intel Xeon Scalable (Skylake) 1st Generation",
          "Intel Xeon E5 v4 (Broadwell E5)",
          "Intel Xeon E5 v3 (Haswell)",
          "Intel Xeon E5 v2 (Ivy Bridge)",
          "Intel Xeon E5 (Sandy Bridge)"
        ],
        "cpu_min_frequency_GHz": [
          "2.0",
          "2.2",
          "2.3",
          "2.5",
          "2.6"
        ],
        "cpu_max_frequency_GHz": [
          "3.5",
          "3.7",
          "3.8",
          "3.5",
          "3.6"
        ],
        "has_local_disk": false,
        "local_disk_size_GB": null,
        "local_num_of_disks": null,
        "local_disk_bus_type": {
          "local_disk_bus_type_id": null,
          "local_disk_bus_type": null
        },
        "local_disk_throughput_MB": null,
        "machine_price_ycu": 5.44
      },
      "machine_volume_conf": {
        "volume_conf_id": 1,
        "name": "volume_gcp_1",
        "encrypted": true,
        "size": 375,
        "disk_type": {
          "disk_type_id": 2,
          "cloud_provider": {
            "cloud_provider_id": 0,
            "name": "GCP"
          },
          "name": "local-ssd",
          "has_fixed_size": true,
          "min_size": 375,
          "max_size": 375
        },
        "machine_volume_num": 1,
        "machine_volume_strip_num": 1,
        "disk_iops": null,
        "disk_throughput_MB": null,
        "disk_num": 1,
        "disk_size": 375
      },
      "created_by": {
        "user_id": 3,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 3,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2024-06-06T09:55:54.581268+00:00",
      "from_date": "2024-06-06T09:55:54.581268+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-conf

```bash
yeedu cluster get-conf -h
```

```bash
usage:  get-conf [-h] [--cluster_conf_id CLUSTER_CONF_ID]
                 [--cluster_conf_name CLUSTER_CONF_NAME]
                 [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_conf_id CLUSTER_CONF_ID
                        Specifies the ID of the cluster configuration to retrieve
                        details.
  --cluster_conf_name CLUSTER_CONF_NAME
                        Specifies the name of the cluster configuration to retrieve
                        details.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-conf example showing the command with either required argument provided.

```bash
yeedu cluster get-conf --cluster_conf_id=9
```

- Console output

```bash
{
  "cluster_conf_id": 9,
  "cluster_conf_name": "n1-highcpu-96",
  "description": null,
  "machine_type_category": "compute_optimized",
  "machine_type": {
    "machine_type_id": 9,
    "cloud_provider": {
      "cloud_provider_id": 0,
      "name": "GCP",
      "description": "Provider for creating infrastructure on Google Cloud Platform"
    },
    "name": "n1-highcpu-96",
    "vCPUs": 96,
    "memory": "86.4 GiB",
    "has_cuda": false,
    "gpu_model": null,
    "gpus": 0,
    "gpu_memory": null,
    "cpu_model": [
      "Intel Xeon Scalable (Skylake) 1st Generation",
      "Intel Xeon E5 v4 (Broadwell E5)",
      "Intel Xeon E5 v3 (Haswell)",
      "Intel Xeon E5 v2 (Ivy Bridge)",
      "Intel Xeon E5 (Sandy Bridge)"
    ],
    "cpu_min_frequency_GHz": [
      "2.0",
      "2.2",
      "2.3",
      "2.5",
      "2.6"
    ],
    "cpu_max_frequency_GHz": [
      "3.5",
      "3.7",
      "3.8",
      "3.5",
      "3.6"
    ],
    "has_local_disk": false,
    "local_disk_size_GB": null,
    "local_num_of_disks": null,
    "local_disk_bus_type": {
      "local_disk_bus_type_id": null,
      "local_disk_bus_type": null
    },
    "local_disk_throughput_MB": null,
    "machine_price_ycu": 32.64
  },
  "machine_volume_conf": {
    "volume_conf_id": 16,
    "name": "volume_gcp_16",
    "encrypted": true,
    "size": 375,
    "disk_type": {
      "disk_type_id": 2,
      "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP"
      },
      "name": "local-ssd",
      "has_fixed_size": true,
      "min_size": 375,
      "max_size": 375
    },
    "machine_volume_num": 16,
    "machine_volume_strip_num": 16,
    "disk_iops": null,
    "disk_throughput_MB": null,
    "disk_num": 1,
    "disk_size": 6000
  },
  "created_by": null,
  "modified_by": null,
  "last_update_date": "2024-05-29T16:09:48.827146+00:00",
  "from_date": "2024-05-29T16:09:48.827146+00:00",
  "to_date": "infinity"
}
```

### edit-conf

```bash
yeedu cluster edit-conf -h
```

```bash
usage:  edit-conf [-h] [--cluster_conf_id CLUSTER_CONF_ID]
                  [--cluster_conf_name CLUSTER_CONF_NAME] [--name [NAME]]
                  [--description [DESCRIPTION]]
                  [--machine_type_category_id MACHINE_TYPE_CATEGORY_ID]
                  [--machine_type_id MACHINE_TYPE_ID] [--volume_conf_id VOLUME_CONF_ID]
                  [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_conf_id CLUSTER_CONF_ID
                        Specifies the ID of the cluster configuration to edit.
  --cluster_conf_name CLUSTER_CONF_NAME
                        Specifies the name of the cluster configuration to edit.
  --name [NAME]         Assigns a new name to the cluster configuration.
  --description [DESCRIPTION]
                        Provides a new description for the cluster configuration.
  --machine_type_category_id MACHINE_TYPE_CATEGORY_ID
                        Sets a new machine type category ID for the cluster
                        configuration.
  --machine_type_id MACHINE_TYPE_ID
                        Sets a new machine type ID for the cluster configuration.
  --volume_conf_id VOLUME_CONF_ID
                        Sets a new volume configuration ID for the cluster configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example of `edit-conf` with the required argument '--cluster_conf_id' and additional optional arguments to update.

```bash
yeedu cluster edit-conf --cluster_conf_id=1 --description="Yeedu General Purpose Configuration"
```

- Console output

```bash
{
  "cluster_conf_id": "242",
  "name": "yeedu_cluster_config",
  "description": "Yeedu General Purpose Configuration",
  "machine_type_category_id": "2",
  "machine_type_id": "1",
  "volume_conf_id": "1",
  "created_by_user_id": "3",
  "modified_by_user_id": "3",
  "last_update_date": "2024-06-06T14:46:44.905Z",
  "from_date": "2024-06-06T09:55:54.581Z",
  "to_date": null
}
```

### delete-conf

```bash
yeedu cluster delete-conf -h
```

```bash
usage:  delete-conf [-h] [--cluster_conf_id CLUSTER_CONF_ID]
                    [--cluster_conf_name CLUSTER_CONF_NAME]
                    [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_conf_id CLUSTER_CONF_ID
                        Specifies the ID of the cluster configuration to delete.
  --cluster_conf_name CLUSTER_CONF_NAME
                        Specifies the name of the cluster configuration to delete.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- delete-conf example with any one of the required argument passed.

```bash
yeedu cluster delete-conf --cluster_conf_name="yeedu_cluster_config"
```

- Console output

```bash
{
  "message": "Deleted Cluster Config Name: 'yeedu_cluster_config'"
}
```

## Cluster Instance

| Command Name                | Utility                                                        |
| --------------------------- | -------------------------------------------------------------- |
| [create](#create)           | Create a new cluster instance.                                 |
| [list](#list)               | List all available cluster instances.                          |
| [search](#search)           | Search for cluster instances based on instance name.           |
| [get](#get)                 | Get details of a specific cluster instance.                    |
| [edit](#edit)               | Modify the configuration of an existing cluster instance.      |
| [start](#start)             | Start a specific cluster instance.                             |
| [stop](#stop)               | Stop a specific cluster instance.                              |
| [destroy](#destroy)         | Destroy a specific cluster instance.                           |
| [disable](#disable)         | Disable a specific cluster instance.                           |
| [enable](#enable)           | Enable a specific cluster instance.                            |
| [get-stats](#get-stats)     | Retrieve Spark job statistics for a specific cluster instance. |
| [list-status](#list-status) | List status events for a specific cluster instance.            |
| [list-errors](#list-errors) | List errors for a specific cluster instance.                   |
| [logs](#logs)               | Download log files for a specific cluster instance.            |

### create

```bash
yeedu cluster create -h
```

```bash
usage:  create [-h] --name [NAME] [--description DESCRIPTION] [--idle_timeout_ms [IDLE_TIMEOUT_MS]] [--labels LABELS [LABELS ...]] [--is_spot_instance [{true,false}]]
               [--metastore_catalog_id METASTORE_CATALOG_ID] [--is_turbo_enabled [{true,false}]] [--disk_type_id [DISK_TYPE_ID]] [--disk_throughput_MB [DISK_THROUGHPUT_MB]] [--disk_iops [DISK_IOPS]] [--enable_public_ip [{true,false}]] [--size [DISK_SIZE]] [--number_of_disks [NUM_OF_DISKS]] 
               [--block_project_ssh_keys [{true,false}]] [--bootstrap_shell_script_file_path BOOTSTRAP_SHELL_SCRIPT_FILE_PATH] --cloud_env_id CLOUD_ENV_ID --object_storage_manager_id OBJECT_STORAGE_MANAGER_ID
               [--conf CONF [CONF ...]] [--packages [PACKAGES]] [--repositories [REPOSITORIES]] [--files [FILES]] [--py-files [PY_FILES]] [--jars [JARS]] [--archives [ARCHIVES]]
               [--env_var ENV_VAR [ENV_VAR ...]] [--conf_secret CONF_SECRET [CONF_SECRET ...]] [--env_var_secret ENV_VAR_SECRET [ENV_VAR_SECRET ...]] --spark_infra_version_id
               SPARK_INFRA_VERSION_ID [--max_parallel_spark_job_execution_per_instance [MAX_PARALLEL_SPARK_JOB_EXECUTION_PER_INSTANCE]] [--num_of_workers [NUM_OF_WORKERS]]
               --cluster_type [YEEDU, STANDALONE, CLUSTER] [--min_instances [MIN_INSTANCES]] [--max_instances [MAX_INSTANCES]] [--clean_up_timeout [CLEAN_UP_TIMEOUT]] --cluster_conf_id
               CLUSTER_CONF_ID [--keep_scratch_disk [{true,false}]] [--cloud_identity [CLOUD_IDENTITY]] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name [NAME]         Provide name to create a cluster instance.
  --description DESCRIPTION
                        Provide description to create a cluster instance.
  --idle_timeout_ms [IDLE_TIMEOUT_MS]
                        Provide idle_timeout_ms to create a cluster instance.
  --labels LABELS [LABELS ...]
                        Provide labels to create a cluster instance.
  --is_spot_instance [{true,false}]
                        Provide is_spot_instance to create a cluster instance. (default: false)
  --metastore_catalog_id METASTORE_CATALOG_ID
                        Provide metastore_catalog_id to attach to a cluster instance (default: None)
  --is_turbo_enabled [{true,false}]
                        Provide is_turbo_engine to create a cluster instance
  --disk_type_id [DISK_TYPE_ID]
                        Provide disk_type to create a cluster instance. 
  --disk_throughput_MB [DISK_THROUGHPUT_MB] 
                        Provide disk_throughput_MB to create a cluster instance. 
  --disk_iops [DISK_IOPS]
                        Provide disk_iops to create a cluster instance. 
  --size [DISK_SIZE]
                        Provide disk_size to create a cluster instance.
  --number_of_disks [NUM_OF_DISKS]
                        Provide num_of_disks to create a cluster.
  --enable_public_ip [{true,false}]
                        Provide enable_public_ip to create a cluster instance. (default: false)
  --block_project_ssh_keys [{true,false}]
                        Provide block_project_ssh_keys to create a cluster instance. (default: true)
  --bootstrap_shell_script_file_path BOOTSTRAP_SHELL_SCRIPT_FILE_PATH
                        Provide bootstrap_shell_script_file_path to create a cluster instance.
  --cloud_env_id CLOUD_ENV_ID
                        Provide cloud_env_id to create a cluster instance.
  --object_storage_manager_id OBJECT_STORAGE_MANAGER_ID
                        Provide object_storage_manager_id to create a cluster instance.
  --conf CONF [CONF ...]
                        Provide conf to create a cluster instance.
  --packages [PACKAGES]
                        Provide packages to create a cluster instance.
  --repositories [REPOSITORIES]
                        Provide repositories to create a cluster instance.
  --files [FILES]       Provide files to create a cluster instance.
  --py-files [PY_FILES]
                        Provide py-files to create a cluster instance.
  --jars [JARS]         Provide jars to create a cluster instance.
  --archives [ARCHIVES]
                        Provide archives to create a cluster instance.
  --env_var ENV_VAR [ENV_VAR ...]
                        Provide env_var to create a cluster instance.
  --conf_secret CONF_SECRET [CONF_SECRET ...]
                        Provide conf_secret to create a cluster instance.
  --env_var_secret ENV_VAR_SECRET [ENV_VAR_SECRET ...]
                        Provide env_var_secret to create a cluster instance.
  --spark_infra_version_id SPARK_INFRA_VERSION_ID
                        Provide spark_infra_version_id to create a cluster instance.
  --max_parallel_spark_job_execution_per_instance [MAX_PARALLEL_SPARK_JOB_EXECUTION_PER_INSTANCE]
                        Provide max_parallel_spark_job_execution_per_instance to create a cluster instance. (default: 5)
  --num_of_workers [NUM_OF_WORKERS]
                        Provide num_of_workers to create a cluster instance.
  --cluster_type [YEEDU, STANDALONE, CLUSTER]
                        Provide cluster_type to create a cluster instance.
  --min_instances [MIN_INSTANCES]
                        Provide min_instances to create a cluster instance.
  --max_instances [MAX_INSTANCES]
                        Provide max_instances to create a cluster instance.
  --clean_up_timeout [CLEAN_UP_TIMEOUT]
                        Provide cleanup_timeout_mins to create a cluster instance. (default: 240)
  --cluster_conf_id CLUSTER_CONF_ID
                        Provide cluster_conf_id to create a cluster instance.
  --keep_scratch_disk [{true,false}]
                        Provide keep_scratch_disk to create a cluster instance.
  --cloud_identity [CLOUD_IDENTITY]
                        Provide cloud_identity to create a cluster instance.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)

```
- create example with all the required and optional arguments passed.

```bash
yeedu cluster create --cluster_conf_id 153 --object_storage_manager_id 159 --name yeedu_cluster_warm_stop --cloud_env_id 156 --spark_infra_version_id 2 --is_turbo_enabled false --cluster_type YEEDU --max_instances 1 --min_instances 1 --keep_scratch_disk false --clean_up_timeout 222 --cloud_identity AWSIamRoleForYeedu
```

- Console output

```bash
{
  "cluster_id": "115",
  "name": "yeedu_cluster_warm_stop",
  "description": null,
  "cloud_env_id": "156",
  "idle_timeout_ms": "600000",
  "labels": {
    "resource": "yeedu",
    "vm": "yeedu_node",
    "tenant_id": "8cee6100-7086-4138-92fd-712046174e91"
  },
  "is_spot_instance": false,
  "enable_public_ip": false,
  "is_turbo_enabled": false,
  "is_cuda_enabled": false,
  "block_project_ssh_keys": false,
  "bootstrap_shell_script": null,
  "object_storage_manager_id": "1",
  "cluster_conf_id": "10",
  "spark_config": {
    "conf": null,
    "packages": null,
    "repositories": null,
    "jars": null,
    "archives": null,
    "env_var": null,
    "conf_secret": null,
    "env_var_secret": null,
    "files": null,
    "py-files": null
  },
  "metastore_catalog_id": null,
  "spark_infra_version_id": "0",
  "engine_cluster_spark_config": {
    "max_parallel_spark_job_execution_per_instance": 5,
    "num_of_workers": null
  },
  "cluster_type": "YEEDU",
  "min_instances": 1,
  "cloud_identity": "AWSIamRoleForYeedu",
  "max_instances": 3,
  "clean_up_timeout": "240",
  "keep_scratch_disk": true,
  "machine_volume_config": {
    "machine_volume_config_id": "58",
    "machine_volume_config_name": "cluster_volume_b064ae83-b9cd-4953-8677-e8019b5550ff",
    "machine_volume_config_description": null,
    "size": "4",
    "encrypted": false,
    "machine_volume_conf_num": 4,
    "machine_volume_conf_strip": 4,
    "number_of_disks": 4,
    "disk_iops": 3000,
    "disk_throughput_MB": 250,
    "disk_type": {
      "disk_type_id": "8",
      "disk_name": "PremiumV2_LRS",
      "cloud_provider_id": "2",
      "has_fixed_size": false,
      "min_size": 1,
      "max_size": 65536,
      "has_fixed_iops": false,
      "min_iops": 3000,
      "max_iops": 80000,
      "has_fixed_throughput": false,
      "min_throughput": 125,
      "max_throughput": 1200
    }
  },
  "tenant_id": "9fcc8aef-3b7f-4495-8ffb-9c35399715a0",
  "created_by_user_id": "8",
  "modified_by_user_id": "8",
  "last_update_date": "2025-06-24T07:24:34.612Z",
  "from_date": "2025-06-24T07:24:34.612Z",
  "to_date": null
}
```

### list

```bash
yeedu cluster list -h
```

```bash
usage:  list [-h] [--cluster_status [CLUSTER_STATUS]] [--cluster_conf_id CLUSTER_CONF_ID] [--cluster_conf_name CLUSTER_CONF_NAME] [--enable [{true,false}]] [--cloud_providers [CLOUD_PROVIDERS]]
             [--cluster_types [CLUSTER_TYPES]] [--spark_infra_version_ids [SPARK_INFRA_VERSION_IDS]] [--machine_type_ids [MACHINE_TYPE_IDS]] [--created_by_ids [CREATED_BY_IDS]]
             [--modified_by_ids [MODIFIED_BY_IDS]] [--page_number PAGE_NUMBER] [--limit LIMIT] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_status [CLUSTER_STATUS]
                        Provide cluster instance status from ["INITIATING", "RUNNING", "STOPPING", "STOPPED", "DESTROYING", "DESTROYED", "ERROR", "RESIZING_UP", "RESIZING_DOWN"] to list, For example
                        --cluster_status="RUNNING,DESTROYED".
  --cluster_conf_id CLUSTER_CONF_ID
                        Provide Cluster Conf Id to list all the Cluster Instances.
  --cluster_conf_name CLUSTER_CONF_NAME
                        Provide Engine Cluster Config Name to list all the Cluster Instances.
  --enable [{true,false}]
                        Provide enable as true or false to list the active or disabled Cluster Instances.
  --cloud_providers [CLOUD_PROVIDERS]
                        Specifies the cloud providers to be used as a filter. Choices are: GCP, AWS, Azure
  --cluster_types [CLUSTER_TYPES]
                        Provide cluster type from ["YEEDU", "STANDALONE", "CLUSTER"] to list, For example --cloud_providers="YEEDU,STANDALONE".
  --spark_infra_version_ids [SPARK_INFRA_VERSION_IDS]
                        To list cluster instance for optional set of spark infra version Ids.
  --machine_type_ids [MACHINE_TYPE_IDS]
                        To list cluster instances for optional set of machine type Ids.
  --created_by_ids [CREATED_BY_IDS]
                        To list cluster instances runs for optional set of created by user Ids.
  --modified_by_ids [MODIFIED_BY_IDS]
                        To list cluster instances for optional set of modified by user Ids.
  --page_number PAGE_NUMBER
                        To list cluster instance for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of cluster instance. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list example with all the optional arguments passed.

```bash
yeedu cluster list --cluster_status DESTROYED --enable true --limit 1
```

- Console output

```bash
{
  "data": [
    {
      "cluster_id": 162,
      "name": "test_cluster_12345_clone",
      "cluster_status": "DESTROYED",
      "cluster_type": "YEEDU",
      "instance_size": 0,
      "min_instances": 1,
      "max_instances": 2,
      "is_turbo_enabled": true,
      "is_cuda_enabled": false,
      "is_spot_instance": true,
      "total_ycu": 0,
      "metastore_catalog": {
        "metastore_catalog_id": 47,
        "metastore_catalog_name": "test55",
        "description": null,
        "metastore_catalog_type": {
          "metastore_catalog_type_id": 1,
          "name": "HIVE",
          "description": null
        }
      },
      "cloud_env": {
        "cloud_env_id": 37,
        "name": "test_cloudenv_gcp",
        "cloud_provider": {
          "cloud_provider_id": 0,
          "name": "GCP"
        }
      },
      "cluster_conf": {
        "cluster_conf_id": 490,
        "cluster_conf_name": "c2d-highcpu-4",
        "machine_type_category": "custom_compute",
        "machine_type": {
          "machine_type_id": 694,
          "name": "c2d-highcpu-4",
          "machine_architecture_type": {
            "machine_architecture_type_id": 0,
            "machine_architecture_type": "x86_64"
          },
          "vCPUs": 4,
          "memory": "8",
          "has_cuda": false,
          "gpu_model": null,
          "gpus": 0,
          "gpu_memory": null,
          "cpu_model": [
            "AMD EPYC Milan"
          ],
          "cpu_min_frequency_GHz": [
            "2.45"
          ],
          "cpu_max_frequency_GHz": [
            "3.5"
          ],
          "has_local_disk": false,
          "local_disk_size_GB": null,
          "local_num_of_disks": null,
          "local_disk_throughput_MB": null,
          "has_spot_instance_support": true,
          "machine_price_ycu": 1.8
        },
        "machine_volume_conf": null
      },
      "spark_infra_version": {
        "spark_infra_version_id": 5,
        "spark_docker_image_name": "v3.5.3-2",
        "spark_version": "3.5.3",
        "hive_version": "2.3.9",
        "hadoop_version": "3.2.4",
        "scala_version": "2.12.15",
        "python_version": "3.9.5",
        "notebook_support": true,
        "has_cuda_support": false,
        "thrift_support": true,
        "yeedu_functions_support": true,
        "has_turbo_support": true,
        "turbo_version": "v1.0.7",
        "has_unity_support": true,
        "unity_version": "v1.0.7",
        "has_hive_support": true,
        "cuda_rapids_version": "23.04.1"
      },
      "engine_cluster_spark_config": {
        "max_parallel_spark_job_execution_per_instance": 1,
        "num_of_workers": null
      },
      "machine_volume_config": null,
      "tenant_id": "c7570bf7-8c36-459b-bfa4-f5afd42ac21b",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2025-09-15T09:55:09.661397+00:00",
      "from_date": "2025-09-15T09:55:09.661397+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 36,
    "total_pages": 36,
    "limit": 1,
    "next_page": 2
  }
}
```

### search

```bash
yeedu cluster search --h
```

```bash
usage:  search [-h] --cluster_name CLUSTER_NAME [--cluster_status [CLUSTER_STATUS]] [--cluster_conf_id CLUSTER_CONF_ID] [--cluster_conf_name CLUSTER_CONF_NAME] [--enable [{true,false}]]
               [--cloud_providers [CLOUD_PROVIDERS]] [--cluster_types [CLUSTER_TYPES]] [--spark_infra_version_ids [SPARK_INFRA_VERSION_IDS]] [--machine_type_ids [MACHINE_TYPE_IDS]]
               [--created_by_ids [CREATED_BY_IDS]] [--modified_by_ids [MODIFIED_BY_IDS]] [--page_number PAGE_NUMBER] [--limit LIMIT] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_name CLUSTER_NAME
                        Provide cluster name to search cluster instances.
  --cluster_status [CLUSTER_STATUS]
                        Provide cluster instance status from ["INITIATING", "RUNNING", "STOPPING", "STOPPED", "DESTROYING", "DESTROYED", "ERROR", "RESIZING_UP", "RESIZING_DOWN"] to list, For example
                        --cluster_status="RUNNING,DESTROYED".
  --cluster_conf_id CLUSTER_CONF_ID
                        Provide Cluster Conf Id to list all the Cluster Instances.
  --cluster_conf_name CLUSTER_CONF_NAME
                        Provide Engine Cluster Config Name to list all the Cluster Instances.
  --enable [{true,false}]
                        Provide enable as true or false to list active or disabled clusters
  --cloud_providers [CLOUD_PROVIDERS]
                        Specifies the cloud providers to be used as a filter. Choices are: GCP, AWS, Azure
  --cluster_types [CLUSTER_TYPES]
                        Provide cluster type from ["YEEDU", "STANDALONE", "CLUSTER"] to list, For example --cluster_types="YEEDU,STANDALONE".
  --spark_infra_version_ids [SPARK_INFRA_VERSION_IDS]
                        To list cluster instance for optional set of spark infra version Ids.
  --machine_type_ids [MACHINE_TYPE_IDS]
                        To list cluster instances for optional set of machine type Ids.
  --created_by_ids [CREATED_BY_IDS]
                        To list cluster instances runs for optional set of created by user Ids.
  --modified_by_ids [MODIFIED_BY_IDS]
                        To list cluster instances for optional set of modified by user Ids.
  --page_number PAGE_NUMBER
                        To search cluster instances for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of cluster instances. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search example with all the optional arguments passed.

```bash
yeedu cluster search --cluster_name yeedu_instance_cli 
```

- Console output

```bash
{
  "data": [
    {
      "cluster_id": 43,
      "name": "yeedu_instance_cli",
      "cluster_status": "INITIATING",
      "cluster_type": "YEEDU",
      "instance_size": 1,
      "min_instances": 1,
      "max_instances": 3,
      "is_turbo_enabled": false,
      "is_cuda_enabled": false,
      "total_ycu": 0,
      "cloud_env": {
        "cloud_env_id": 1,
        "name": "gcp_env",
        "cloud_provider": {
          "cloud_provider_id": 0,
          "name": "GCP"
        }
      },
      "cluster_conf": {
        "cluster_conf_id": 10,
        "cluster_conf_name": "n1-standard-4",
        "machine_type_category": "general_purpose",
        "machine_type": {
          "machine_type_id": 10,
          "name": "n1-standard-4",
          "machine_architecture_type": {
            "machine_architecture_type_id": 0,
            "machine_architecture_type": "x86_64"
          },
          "vCPUs": 4,
          "memory": "15 GiB",
          "has_cuda": false,
          "gpu_model": null,
          "gpus": 0,
          "gpu_memory": null,
          "cpu_model": [
            "Intel Xeon Scalable (Skylake) 1st Generation",
            "Intel Xeon E5 v4 (Broadwell E5)",
            "Intel Xeon E5 v3 (Haswell)",
            "Intel Xeon E5 v2 (Ivy Bridge)",
            "Intel Xeon E5 (Sandy Bridge)"
          ],
          "cpu_min_frequency_GHz": [
            "2.0",
            "2.2",
            "2.3",
            "2.5",
            "2.6"
          ],
          "cpu_max_frequency_GHz": [
            "3.5",
            "3.7",
            "3.8",
            "3.5",
            "3.6"
          ],
          "has_local_disk": false,
          "local_disk_size_GB": null,
          "local_num_of_disks": null,
          "local_disk_throughput_MB": null,
          "has_spot_instance_support": true,
          "machine_price_ycu": 2.5
        },
        "machine_volume_conf": {
          "volume_conf_id": 2,
          "name": "volume_gcp_2",
          "size": 375,
          "machine_volume_num": 2,
          "machine_volume_strip_num": 2
        }
      },
      "spark_infra_version": {
        "spark_infra_version_id": 0,
        "spark_docker_image_name": "2.4.8",
        "spark_version": "2.4.8",
        "hive_version": "1.2.1",
        "hadoop_version": "2.10.1",
        "scala_version": "2.11.12",
        "python_version": "2.7.18",
        "notebook_support": false,
        "has_cuda_support": false,
        "thrift_support": false,
        "yeedu_functions_support": false,
        "has_turbo_support": false,
        "turbo_version": null,
        "has_unity_support": false,
        "unity_version": null,
        "has_hive_support": true,
        "cuda_rapids_version": null
      },
      "engine_cluster_spark_config": {
        "max_parallel_spark_job_execution_per_instance": 5,
        "num_of_workers": null
      },
      "machine_volume_config": {
        "volume_conf_id": 58,
        "name": "cluster_volume_b064ae83-b9cd-4953-8677-e8019b5550ff",
        "machine_volume_num": 4,
        "machine_volume_strip_num": 4,
        "number_of_disks": 4,
        "size": 4,
        "disk_iops": 3000,
        "disk_throughput_mb": 250,
        "disk_type": {
          "disk_type_id": 8,
          "name": "PremiumV2_LRS",
          "cloud_provider": {
            "cloud_provider_id": 2,
            "name": "Azure"
          },
          "has_fixed_size": false,
          "min_size": 1,
          "max_size": 65536,
          "has_fixed_throughput": false,
          "min_throughput": 125,
          "max_throughput": 1200,
          "has_fixed_iops": false,
          "min_iops": 3000,
          "max_iops": 80000
        }
      },
      "tenant_id": "9fcc8aef-3b7f-4495-8ffb-9c35399715a0",
      "created_by": {
        "user_id": 8,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 8,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2025-06-24T07:24:34.612638+00:00",
      "from_date": "2025-06-24T07:24:34.612638+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get

```bash
yeedu cluster get -h
```

```bash
usage:  get [-h] [--cluster_id CLUSTER_ID] [--cluster_name CLUSTER_NAME]
            [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide cluster instance id to get information about a specific
                        cluster instance.
  --cluster_name CLUSTER_NAME
                        Provide cluster instance name to get information about a specific
                        cluster instance.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get example with any one of the required argument '--cluster_name' passed.

```bash
yeedu cluster get --cluster_id 43
```

- Console output

```bash
{
  "cluster_id": 43,
  "name": "yeedu_instance_cli",
  "description": "Test yeedu instance",
  "labels": {
    "resource": "yeedu",
    "vm": "yeedu_node",
    "tenant_id": "9fcc8aef-3b7f-4495-8ffb-9c35399715a0"
  },
  "idle_timeout_ms": 1200000,
  "cluster_status": "INITIATING",
  "cluster_type": "YEEDU",
  "instance_size": 1,
  "is_spot_instance": false,
  "enable_public_ip": false,
  "block_project_ssh_keys": false,
  "min_instances": 1,
  "max_instances": 3,
  "total_ycu": 0,
  "clean_up_timeout": 240,
  "keep_scratch_disk": true,
  "cloud_identity": "AWSIamRoleForYeedu",
  "is_turbo_enabled": true,
  "is_cuda_enabled": false,
  "bootstrap_shell_script": null,
  "cluster_conf": {
    "cluster_conf_id": 10,
    "cluster_conf_name": "n1-standard-4",
    "description": null,
    "machine_type_category": "general_purpose",
    "machine_type": {
      "machine_type_id": 10,
      "name": "n1-standard-4",
      "machine_architecture_type": {
        "machine_architecture_type_id": 0,
        "machine_architecture_type": "x86_64"
      },
      "vCPUs": 4,
      "memory": "15 GiB",
      "has_cuda": false,
      "gpu_model": null,
      "gpus": 0,
      "gpu_memory": null,
      "cpu_model": [
        "Intel Xeon Scalable (Skylake) 1st Generation",
        "Intel Xeon E5 v4 (Broadwell E5)",
        "Intel Xeon E5 v3 (Haswell)",
        "Intel Xeon E5 v2 (Ivy Bridge)",
        "Intel Xeon E5 (Sandy Bridge)"
      ],
      "cpu_min_frequency_GHz": [
        "2.0",
        "2.2",
        "2.3",
        "2.5",
        "2.6"
      ],
      "cpu_max_frequency_GHz": [
        "3.5",
        "3.7",
        "3.8",
        "3.5",
        "3.6"
      ],
      "has_local_disk": false,
      "local_disk_size_GB": null,
      "local_num_of_disks": null,
      "local_disk_bus_type": {
        "local_disk_bus_type_id": null,
        "local_disk_bus_type": null
      },
      "local_disk_throughput_MB": null,
      "has_spot_instance_support": true,
      "machine_price_ycu": 2.5
    },
    "machine_volume_conf": {
      "volume_conf_id": 2,
      "name": "volume_gcp_2",
      "description": null,
      "encrypted": true,
      "size": 375,
      "disk_type": {
        "disk_type_id": 2,
        "cloud_provider_id": 0,
        "name": "local-ssd",
        "has_fixed_size": true,
        "min_size": 375,
        "max_size": 375,
        "has_fixed_iops": true,
        "min_iops": 170000,
        "max_iops": 3200000,
        "has_fixed_throughput": true,
        "min_throughput": 660,
        "max_throughput": 12480
      },
      "machine_volume_num": 2,
      "machine_volume_strip_num": 2,
      "disk_iops": 170000,
      "disk_throughput_MB": 660,
      "disk_num": 1,
      "disk_size": 750
    }
  },
  "cloud_env": {
    "cloud_env_id": 1,
    "cloud_env_name": "gcp_env",
    "description": null,
    "cloud_provider": {
      "cloud_provider_id": 0,
      "name": "GCP",
      "description": "Provider for creating infrastructure on Google Cloud Platform"
    },
    "availability_zone": {
      "availability_zone_id": 75,
      "name": "us-central1-a",
      "cloud_provider_id": 0,
      "region": "us-central1",
      "description": "Council Bluffs, Iowa, North America"
    },
    "network_config": {
      "network_conf_id": 1,
      "network_conf_name": "gcp_network",
      "description": null,
      "network_project_id": "yeedu",
      "network_name": "yeedusparkvpc",
      "network_tags": [
        "yeedu",
        "iap-allow"
      ],
      "subnet": "custom-subnet-yeedu",
      "availability_zone": {
        "availability_zone_id": 75,
        "name": "us-central1-a",
        "cloud_provider_id": 0,
        "region": "us-central1",
        "description": "Council Bluffs, Iowa, North America"
      }
    },
    "cloud_project": "yeedu",
    "credentials_config": {
      "credentials_conf_id": 1,
      "credentials_conf_name": "gcp_credential",
      "description": null,
      "credential_type": {
        "credential_type_id": 0,
        "name": "Google Service Account",
        "cloud_provider_id": 0
      }
    },
    "boot_disk_image": {
      "boot_disk_image_id": 9,
      "boot_disk_image_name": "gcp_22_04",
      "description": null,
      "cloud_provider_id": 0,
      "linux_distro": {
        "linux_distro_id": 1,
        "distro_name": "UBUNTU",
        "distro_version": "22.04 LTS"
      },
      "boot_disk_image": "ubuntu-os-cloud/ubuntu-2204-lts"
    }
  },
  "spark_infra_version": {
    "spark_infra_version_id": 0,
    "spark_docker_image_name": "2.4.8",
    "spark_version": "2.4.8",
    "hive_version": "1.2.1",
    "hadoop_version": "2.10.1",
    "scala_version": "2.11.12",
    "python_version": "2.7.18",
    "notebook_support": false,
    "has_cuda_support": false,
    "thrift_support": false,
    "yeedu_functions_support": false,
    "has_turbo_support": false,
    "turbo_version": null,
    "has_unity_support": false,
    "unity_version": null,
    "has_hive_support": true,
    "cuda_rapids_version": null
  },
  "metastore_catalog": {
    "metastore_catalog_id": null,
    "metastore_catalog_name": null,
    "description": null,
    "metastore_catalog_type": {
      "metastore_catalog_type_id": null,
      "name": null,
      "description": null
    }
  },
  "spark_config": {
    "conf": [],
    "packages": [],
    "repositories": [],
    "jars": [],
    "archives": [],
    "env_var": [],
    "conf_secret": null,
    "env_var_secret": null,
    "files": [],
    "py-files": []
  },
  "engine_cluster_spark_config": {
    "max_parallel_spark_job_execution_per_instance": 5,
    "num_of_workers": null
  },
  "object_storage_manager": {
    "object_storage_manager_id": 1,
    "object_storage_manager_name": "gcp_osm",
    "description": null,
    "credentials_config": {
      "credential_config_id": 1,
      "name": "gcp_credential",
      "description": null,
      "credential_type_name": "Google Service Account"
    },
    "object_storage_bucket_name": "yeedu-qa"
  },
  "machine_volume_config": {
    "volume_conf_id": 58,
    "name": "cluster_volume_b064ae83-b9cd-4953-8677-e8019b5550ff",
    "machine_volume_num": 4,
    "machine_volume_strip_num": 4,
    "number_of_disks": 4,
    "size": 4,
    "disk_iops": 3000,
    "disk_throughput_mb": 250,
    "disk_type": {
      "disk_type_id": 8,
      "name": "PremiumV2_LRS",
      "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP"
      },
      "has_fixed_size": false,
      "min_size": 1,
      "max_size": 65536,
      "has_fixed_throughput": false,
      "min_throughput": 125,
      "max_throughput": 1200,
      "has_fixed_iops": false,
      "min_iops": 3000,
      "max_iops": 80000
    }
  },
  "workflow_job_instance_details": {
    "workflow_job_instance_status": {
      "workflow_job_instance_id": 535765,
      "workflow_job_id": 535765,
      "status": "SENT",
      "from_date": "2025-06-24T07:24:34.612638+00:00",
      "to_date": "infinity"
    }
  },
  "tenant_id": "9fcc8aef-3b7f-4495-8ffb-9c35399715a0",
  "created_by": {
    "user_id": 8,
    "username": "ysu0000@yeedu.io"
  },
  "modified_by": {
    "user_id": 8,
    "username": "ysu0000@yeedu.io"
  },
  "last_update_date": "2025-06-24T07:24:34.612638+00:00",
  "from_date": "2025-06-24T07:24:34.612638+00:00",
  "to_date": "infinity"
}
```

### edit

```bash
yeedu cluster edit -h
```

```bash
$ yeedu cluster edit -h
usage:  edit [-h] [--cluster_id CLUSTER_ID]
             [--cluster_name CLUSTER_NAME] [--name NAME]
             [--metastore_catalog_id METASTORE_CATALOG_ID]
             [--description DESCRIPTION]
             [--idle_timeout_ms [IDLE_TIMEOUT_MS]]
             [--labels LABELS [LABELS ...]]
             [--is_spot_instance [{true,false}]]
             [--enable_public_ip [{true,false}]]
             [--is_turbo_enabled [{true,false}]]
             [--disk_type_id [DISK_TYPE_ID]] 
             [--disk_throughput_MB [DISK_THROUGHPUT_MB]] 
             [--disk_iops [DISK_IOPS]] 
             [--size [DISK_SIZE]] 
             [--number_of_disks [NUM_OF_DISKS]]
             [--block_project_ssh_keys [{true,false}]]
             [--bootstrap_shell_script_file_path [BOOTSTRAP_SHELL_SCRIPT_FILE_PATH]]
             [--cloud_env_id [CLOUD_ENV_ID]]
             [--object_storage_manager_id [OBJECT_STORAGE_MANAGER_ID]]
             [--spark_infra_version_id SPARK_INFRA_VERSION_ID]
             [--cluster_conf_id [CLUSTER_CONF_ID]]
             [--conf CONF [CONF ...]] [--packages [PACKAGES]]
             [--repositories [REPOSITORIES]] [--jars [JARS]]
             [--archives [ARCHIVES]] [--files [FILES]]
             [--py-files [PY_FILES]]
             [--env_var ENV_VAR [ENV_VAR ...]]
             [--conf_secret CONF_SECRET [CONF_SECRET ...]]
             [--env_var_secret ENV_VAR_SECRET [ENV_VAR_SECRET ...]]
             [--max_parallel_spark_job_execution_per_instance [MAX_PARALLEL_SPARK_JOB_EXECUTION_PER_INSTANCE]]
             [--num_of_workers [NUM_OF_WORKERS]]
             [--min_instances [MIN_INSTANCES]]
             [--max_instances [MAX_INSTANCES]]
             [--clean_up_timeout [CLEAN_UP_TIMEOUT]]
             [--keep_scratch_disk [{true,false}]]
             [--cloud_identity [CLOUD_IDENTITY]]
             [--json-output [{pretty,default}]]
             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide a specific cluster instance id to
                        edit.
  --cluster_name CLUSTER_NAME
                        Provide a specific cluster instance name to
                        edit.
  --name NAME           Provide name to edit a cluster instance.
  --metastore_catalog_id METASTORE_CATALOG_ID
                        Provide metastore_catalog_id to attach to a cluster instance (default: None)
  --description DESCRIPTION
                        Provide description to edit a cluster
                        instance.
  --idle_timeout_ms [IDLE_TIMEOUT_MS]
                        Provide idle_timeout_ms to edit a cluster
                        instance.
  --labels LABELS [LABELS ...]
                        Provide labels to edit a cluster instance.
  --is_spot_instance [{true,false}]
                        Provide is_spot_instance to edit a cluster instance. (default: None)
  --enable_public_ip [{true,false}]
                        Provide enable_public_ip to edit a cluster
                        instance.
  --is_turbo_enabled [{true,false}]
                        Provide is_turbo_enabled to edit a cluster
                        instance.
  --disk_type_id [DISK_TYPE_ID]
                        Provide disk_type to edit a cluster instance. 
  --disk_throughput_MB [DISK_THROUGHPUT_MB] 
                        Provide disk_throughput_MB to edit a cluster instance. 
  --disk_iops [DISK_IOPS]
                        Provide disk_iops to edit a cluster instance. 
  --size [DISK_SIZE]
                        Provide disk_size to edit a cluster instance.
  --number_of_disks [NUM_OF_DISKS]
                        Provide num_of_disks to edit a cluster.
  --block_project_ssh_keys [{true,false}]
                        Provide block_project_ssh_keys to edit a
                        cluster instance.
  --bootstrap_shell_script_file_path [BOOTSTRAP_SHELL_SCRIPT_FILE_PATH]
                        Provide bootstrap_shell_script_file_path to
                        edit a cluster instance.
  --cloud_env_id [CLOUD_ENV_ID]
                        Provide cloud_env_id to edit a cluster
                        instance.
  --object_storage_manager_id [OBJECT_STORAGE_MANAGER_ID]
                        Provide object_storage_manager_id to edit a
                        cluster instance.
  --spark_infra_version_id SPARK_INFRA_VERSION_ID
                        Provide spark_infra_version_id to edit a
                        cluster instance.
  --cluster_conf_id [CLUSTER_CONF_ID]
                        Provide cluster_conf_id to edit a cluster
                        instance.
  --conf CONF [CONF ...]
                        Provide conf to edit a cluster instance.
  --packages [PACKAGES]
                        Provide packages to edit a cluster instance.
  --repositories [REPOSITORIES]
                        Provide repositories to edit a cluster
                        instance.
  --jars [JARS]         Provide jars to edit a cluster instance.
  --archives [ARCHIVES]
                        Provide archives to edit a cluster instance.
  --files [FILES]       Provide files to edit a cluster instance.
  --py-files [PY_FILES]
                        Provide py-files to edit a cluster instance.
  --env_var ENV_VAR [ENV_VAR ...]
                        Provide env_var to edit a cluster instance.
  --conf_secret CONF_SECRET [CONF_SECRET ...]
                        Provide conf_secret to edit a cluster
                        instance.
  --env_var_secret ENV_VAR_SECRET [ENV_VAR_SECRET ...]
                        Provide env_var_secret to edit a cluster
                        instance.
  --max_parallel_spark_job_execution_per_instance [MAX_PARALLEL_SPARK_JOB_EXECUTION_PER_INSTANCE]
                        Provide max_parallel_spark_job_execution_per
                        _instance to edit a cluster instance.
  --num_of_workers [NUM_OF_WORKERS]
                        Provide num_of_workers to edit a cluster
                        instance.
  --min_instances [MIN_INSTANCES]
                        Provide min_instances to edit a cluster
                        instance.
  --max_instances [MAX_INSTANCES]
                        Provide max_instances to edit a cluster
                        instance.
  --clean_up_timeout [CLEAN_UP_TIMEOUT]
                        Provide cleanup_timeout_mins to edit a
                        cluster instance.
  --keep_scratch_disk [{true,false}]
                        Provide keep_scratch_disk to edit a cluster
                        instance.
  --cloud_identity [CLOUD_IDENTITY]
                        Provide cloud_identity to edit a cluster
                        instance.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output.
                        (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if
                        set to 'true'. (default: false)
```

- edit example with one of the required '--cluster_id' argument and other optional argument is passed which is to be updated.

```bash
yeedu cluster edit --cluster_id 43 --size 6
```

- Console output

```bash
{
  "cluster_id": "43",
  "name": "yeedu_instance_cli",
  "description": "Test yeedu instance",
  "cloud_env_id": "1",
  "idle_timeout_ms": "1200000",
  "labels": {
    "resource": "yeedu",
    "vm": "yeedu_node",
    "tenant_id": "9fcc8aef-3b7f-4495-8ffb-9c35399715a0"
  },
  "is_spot_instance": false,
  "enable_public_ip": false,
  "block_project_ssh_keys": false,
  "bootstrap_shell_script": null,
  "object_storage_manager_id": "1",
  "cluster_conf_id": "10",
  "spark_config_id": "43",
  "metastore_catalog_id": null,
  "spark_infra_version_id": "0",
  "is_turbo_enabled": false,
  "is_cuda_enabled": false,
  "spark_config": {
    "conf": null,
    "packages": null,
    "repositories": null,
    "jars": null,
    "archives": null,
    "env_var": null,
    "conf_secret": null,
    "env_var_secret": null,
    "files": null,
    "py-files": null
  },
  "engine_cluster_spark_config": {
    "max_parallel_spark_job_execution_per_instance": 5
  },
  "cluster_type": "YEEDU",
  "min_instances": 1,
  "max_instances": 3,
  "clean_up_timeout": "240",
  "keep_scratch_disk": true,
  "cloud_identity": "AWSIamRoleForYeedu",
  "machine_volume_config": {
    "machine_volume_config_id": "58",
    "machine_volume_config_name": "cluster_volume_b064ae83-b9cd-4953-8677-e8019b5550ff",
    "machine_volume_config_description": null,
    "size": "6",
    "encrypted": false,
    "machine_volume_conf_num": 4,
    "machine_volume_conf_strip": 4,
    "number_of_disks": 4,
    "disk_iops": 3000,
    "disk_throughput_MB": 250,
    "disk_type": {
      "disk_type_id": "8",
      "disk_name": "PremiumV2_LRS",
      "cloud_provider_id": "2",
      "has_fixed_size": false,
      "min_size": 1,
      "max_size": 65536,
      "has_fixed_iops": false,
      "min_iops": 3000,
      "max_iops": 80000,
      "has_fixed_throughput": false,
      "min_throughput": 125,
      "max_throughput": 1200
    }
  },
  "tenant_id": "9fcc8aef-3b7f-4495-8ffb-9c35399715a0",
  "created_by_user_id": "8",
  "modified_by_user_id": "8",
  "last_update_date": "2025-06-24T08:03:34.888Z",
  "from_date": "2025-06-24T07:24:34.612Z",
  "to_date": null
}
```

### start

```bash
yeedu cluster start -h
```

```bash
usage:  start [-h] [--cluster_id CLUSTER_ID] [--cluster_name CLUSTER_NAME]
              [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide cluster instance id to start a cluster instance.
  --cluster_name CLUSTER_NAME
                        Provide cluster instance name to start a cluster instance.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- start example with one of the required argument '--cluster_id' passed.

```bash
yeedu cluster start --cluster_id=1
```

- Console output

```bash
{
  "CosiStart": {
    "workflow_job_id": 1,
    "workflow_job_instance_id": 1,
    "engine_cluster_instance_id": 1
  }
}
```

### stop

```bash
yeedu cluster stop -h
```

```bash
usage:  stop [-h] [--cluster_id CLUSTER_ID]
             [--cluster_name CLUSTER_NAME]
             [--json-output [{pretty,default}]]
             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide cluster instance id to stop a
                        cluster instance.
  --cluster_name CLUSTER_NAME
                        Provide cluster instance name to stop a
                        cluster instance.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output.
                        (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if
                        set to 'true'. (default: false)
```

- stop example with one of the required argument '--cluster_id' passed.

```bash
yeedu cluster stop --cluster_id 4
```

- Console output

```bash
{
  "CosiStop": {
    "workflow_job_id": "12662",
    "workflow_job_instance_id": "12662",
    "engine_cluster_instance_id": 11
  }
}
```

### destroy

```bash
yeedu cluster destroy -h
```

```bash
usage:  destroy [-h] [--cluster_id CLUSTER_ID] [--cluster_name CLUSTER_NAME]
                [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide cluster instance id to destroy a cluster instance.
  --cluster_name CLUSTER_NAME
                        Provide cluster instance name to destroy a cluster instance.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- destroy example with one of the required argument '--cluster_id' passed.

```bash
yeedu cluster destroy --cluster_id=1
```

- Console output

```bash
{
  "CosiDestroy": {
    "workflow_job_id": 1,
    "workflow_job_instance_id": 1,
    "engine_cluster_instance_id": 1
  }
}
```

### disable

```bash
yeedu cluster disable -h
```

```bash
usage:  disable [-h] [--cluster_id CLUSTER_ID]
                [--cluster_name CLUSTER_NAME]
                [--json-output [{pretty,default}]]
                [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide cluster instance id to disable a
                        cluster instance.
  --cluster_name CLUSTER_NAME
                        Provide cluster instance name to disable a
                        cluster instance.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set
                        to 'true'. (default: false)
```

- disable example with one of the required argument '--cluster_id' passed.

```bash
yeedu cluster disable --cluster_id=10
```

- Console output

```bash
{
  "message": "The cluster_id: '10' has been disabled successfully."
}
```

### enable

```bash
yeedu cluster enable -h
```

```bash
usage:  enable [-h] [--cluster_id CLUSTER_ID]
               [--cluster_name CLUSTER_NAME]
               [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide cluster instance id to enable a cluster
                        instance.
  --cluster_name CLUSTER_NAME
                        Provide cluster instance name to enable a
                        cluster instance.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set
                        to 'true'. (default: false)
```

- enable example with one of the required argument '--cluster_id' passed.

```bash
yeedu cluster enable --cluster_id=10
```

- Console output

```bash
{
  "id": "10",
  "name": "yeedu_instance_cls",
  "description": "yeedu",
  "cloud_env_id": "82",
  "idle_timeout_ms": "604800000",
  "labels": {
    "resource": "yeedu",
    "vm": "yeedu_node",
    "tenant_id": "8cee6100-7086-4138-92fd-712046174e91"
  },
  "is_spot_instance": false,
  "metastore_catalog_id": 0,
  "is_turbo_enabled": false,
  "disk_type_id": "0",
  "disk_throughput_MB": null,
  "disk_iops": null,
  "size": 125,
  "number_of_disks": 2,
  "enable_public_ip": false,
  "block_project_ssh_keys": false,
  "bootstrap_shell_script": "#!/bin/bash\n",
  "object_storage_manager_id": "1",
  "engine_cluster_config_id": "1",
  "spark_config_id": "10",
  "hive_metastore_id": null,
  "spark_infra_version_id": "0",
  "engine_cluster_spark_config_id": "10",
  "cluster_type_id": "0",
  "min_instances": 1,
  "max_instances": 2,
  "clean_up_timeout": "240",
  "keep_scratch_disk": false,
  "cloud_identity": "AWSIamRoleForYeedu",
  "tenant_id": "8cee6100-7086-4138-92fd-712046174e91",
  "created_by_user_id": "13",
  "modified_by_user_id": "32",
  "last_update_date": "2025-02-04T13:41:10.974Z",
  "from_date": "2024-01-22T18:54:13.877Z",
  "to_date": null
}
```

### get-stats

```bash
yeedu cluster get-stats -h
```

```bash
usage:  get-stats [-h] [--cluster_id CLUSTER_ID] [--cluster_name CLUSTER_NAME]
                  [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide cluster instance id to get the spark job statistics of a
                        cluster instance.
  --cluster_name CLUSTER_NAME
                        Provide cluster instance name to get the spark job statistics of
                        a cluster instance.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-stats example with one of the optional arguments '--cluster_name' passed.

```bash
yeedu cluster get-stats --cluster_name="yeedu_cluster_instance"
```

- Console output

```bash
{
  "SUBMITTED": 1,
  "RUNNING": 2,
  "DONE": 4,
  "ERROR": 0,
  "TERMINATED": 0,
  "STOPPING": 1,
  "STOPPED": 1,
  "TOTAL_JOB_COUNT": 9
}
```

### list-status

```bash
yeedu cluster list-status -h
```

```bash
usage:  list-status [-h] [--cluster_id CLUSTER_ID] [--cluster_name CLUSTER_NAME]
                    [--page_number PAGE_NUMBER] [--limit LIMIT]
                    [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide cluster id to list all the cluster instance status.
  --cluster_name CLUSTER_NAME
                        Provide cluster name to list all the cluster instance status.
  --page_number PAGE_NUMBER
                        To list the cluster instance status for a specific page_number.
                        (default: 1)
  --limit LIMIT         Provide limit to list number of cluster instance status.
                        (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-status example with one of the required argument '--cluster_id' and other optional argument passed.

```bash
yeedu cluster list-status --cluster_id=1 --limit=4
```

- Console output

```bash
{
  "data": [
    {
      "cluster_status_id": 185,
      "cluster_status": "INITIATING",
      "current_node_size": 1,
      "created_by": "ysu0000@yeedu.io",
      "start_time": "2024-06-06T12:08:09.501317+00:00",
      "end_time": "infinity"
    },
    {
      "cluster_status_id": 164,
      "cluster_status": "STOPPED",
      "current_node_size": 0,
      "created_by": null,
      "start_time": "2024-06-03T13:41:13.403337+00:00",
      "end_time": "2024-06-06T12:08:09.577+00:00"
    },
    {
      "cluster_status_id": 163,
      "cluster_status": "STOPPING",
      "current_node_size": 0,
      "created_by": "ysu0001@yeedu.io",
      "start_time": "2024-06-03T13:39:52.903881+00:00",
      "end_time": "2024-06-03T13:41:13.403337+00:00"
    },
    {
      "cluster_status_id": 160,
      "cluster_status": "RUNNING",
      "current_node_size": 1,
      "created_by": null,
      "start_time": "2024-06-03T09:04:56.679352+00:00",
      "end_time": "2024-06-03T13:39:52.916+00:00"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 41,
    "total_pages": 11,
    "limit": 4,
    "next_page": 2
  }
}
```

### stop-all-jobs

```bash
yeedu cluster stop-all-jobs -h
```

```bash
usage:  stop-all-jobs [-h] --cluster_id CLUSTER_ID [--json-output [{pretty,default}]]
                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Specifies the ID of the cluster instance to stop all the jobs.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- stop-all-jobs example with the required argument '--cluster_id' passed.

```bash
yeedu cluster stop-all-jobs --cluster_id=1
```

- Console output

```bash
{
  "CosiKillAllJobsByCluster": {
    "workflow_job_id": 0,
    "workflow_job_instance_id": 0,
    "engine_cluster_instance_id": 1,
    "created_by_user_id": 1
  }
}
```

### list-errors

```bash
yeedu cluster list-errors -h
```

```bash
usage:  list-errors [-h] [--cluster_id CLUSTER_ID]
                    [--cluster_status_id CLUSTER_STATUS_ID] [--page_number PAGE_NUMBER]
                    [--limit LIMIT] [--json-output [{pretty,default}]]
                    [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide cluster id to list all the cluster errors.
  --cluster_status_id CLUSTER_STATUS_ID
                        Provide Cluster Status Id to list all the cluster errors.
  --page_number PAGE_NUMBER
                        To list all the cluster errors for a specific page_number.
                        (default: 1)
  --limit LIMIT         Provide limit to list number of cluster errors. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-errors example with one of the required argument '--cluster_id' passed.

```bash
yeedu cluster list-errors --cluster_id=1
```

- Console output

```bash
{
  "error_code": "RFA-000043",
  "error_message": "No workflow instance errors found for the provided cluster instance id: 1."
}
```

### logs

```bash
yeedu cluster logs -h
```

```bash
usage:  logs [-h] [--cluster_id CLUSTER_ID] [--cluster_name CLUSTER_NAME] [--log_type {stdout,stderr}] [--cluster_status_id CLUSTER_STATUS_ID] [--last_n_lines LAST_N_LINES] [--file_size_bytes FILE_SIZE_BYTES] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide Cluster Instance Id to download log records.
  --cluster_name CLUSTER_NAME
                        Provide Cluster Instance Name to download log records.
  --log_type {stdout,stderr}
                        Provide log_type to download Cluster Instance log records. (default: stdout)
  --cluster_status_id CLUSTER_STATUS_ID
                        Provide Cluster Status Id to download log records.
  --last_n_lines LAST_N_LINES
                        Number of lines to retrieve from the end of the log file (sample preview).
  --file_size_bytes FILE_SIZE_BYTES
                        Number of bytes to preview from the beginning of the log file (sample preview).
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)

```

- logs example with one of the required '--cluster_id' argument passed.

```bash
yeedu cluster logs --cluster_id=1
```

- Console output

```bash
Initializing modules...
- local-node in module
- master-standalone-cluster in module
- standalone-node in module
- worker-standalone-cluster in module
Initializing the backend...

Successfully configured the backend "pg"! Terraform will automatically
use this backend unless the backend configuration changes.
Initializing provider plugins...
- Finding latest version of hashicorp/random...
- Finding latest version of hashicorp/template...
- Finding latest version of hashicorp/google...
- Installing hashicorp/template v2.2.0...
- Installed hashicorp/template v2.2.0 (signed by HashiCorp)
- Installing hashicorp/google v4.50.0...
- Installed hashicorp/google v4.50.0 (signed by HashiCorp)
- Installing hashicorp/random v3.4.3...
- Installed hashicorp/random v3.4.3 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.
Terraform has been successfully initialized!

...

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:
local-node-uuids = [
  {
    "instance_uuid" = tomap({
      "292a79d6-7967-3284-6e19-31aecf9977f4" = 0
    })
    "reserved_ip" = [
      "10.101.1.41",
    ]
  },
]
master-standalone-cluster-uuids = []
standalone-node-uuids = []
worker-standalone-cluster-uuids = []
```

## Cluster Access Control

| Command Name                                            | Utility                                        |
| ------------------------------------------------------- | ---------------------------------------------- |
| [associate-workspace](#associate-workspace)             | Associate a cluster with a workspace.          |
| [dissociate-workspace](#dissociate-workspace)           | Dissociate a cluster from a workspace.         |
| [list-workspaces](#list-workspaces)                     | List all workspaces associated with a cluster. |
| [search-workspaces](#search-workspaces)                 | Search workspaces associated with a cluster.   |
| [list-workspace-clusters](#list-workspace-clusters)     | List all clusters associated with a workspace. |
| [search-workspace-clusters](#search-workspace-clusters) | Search clusters associated with a workspace.   |

### associate-workspace

```bash
yeedu cluster associate-workspace -h
```

```bash
usage:  associate-workspace [-h] --workspace_id WORKSPACE_ID --cluster_id CLUSTER_ID
                            [--json-output [{pretty,default}]]
                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to associate it with a cluster.
  --cluster_id CLUSTER_ID
                        Provide Cluster Id to to associate it with a workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- associate-workspace example with all the required arguments passed.

```bash
yeedu cluster associate-workspace --workspace_id=1 --cluster_id=1
```

- Console output

```bash
{
  "workspace_id": "1",
  "cluster_id": "1",
  "created_by_user_id": "3",
  "modified_by_user_id": "3",
  "last_update_date": "2024-06-07T10:46:31.979Z",
  "from_date": "2024-06-07T10:46:31.979Z",
  "to_date": null
}
```

### dissociate-workspace

```bash
yeedu cluster dissociate-workspace -h
```

```bash
usage:  dissociate-workspace [-h] --workspace_id WORKSPACE_ID --cluster_id CLUSTER_ID
                             [--json-output [{pretty,default}]]
                             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to dissociate it with a cluster.
  --cluster_id CLUSTER_ID
                        Provide Cluster Id to dissociate it with a workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- dissociate-workspace example with all the required arguments passed.

```bash
yeedu cluster dissociate-workspace --workspace_id=1 --cluster_id=1
```

- Console output

```bash
{
  "message": "Deleted Cluster and Workspace association successfully."
}
```

### list-workspaces

```bash
yeedu cluster list-workspaces -h
```

```bash
usage:  list-workspaces [-h] --cluster_id CLUSTER_ID [--page_number PAGE_NUMBER]
                        [--limit LIMIT] [--json-output [{pretty,default}]]
                        [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide Cluster Id to list all the associated workspaces.
  --page_number PAGE_NUMBER
                        To list Clusters for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of Clusters. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-workspaces example with the required and optional arguments passed.

```bash
yeedu cluster list-workspaces --cluster_id=1 --limit=2
```

- Console output

```bash
{
  "data": [
    {
      "workspace": {
        "workspace_id": 2,
        "name": "notebook_testing",
        "description": null
      },
      "cluster_info": {
        "cluster_id": 1,
        "name": "notebook_testing_by_me",
        "cluster_status": "DESTROYED",
        "cluster_type": "YEEDU",
        "instance_size": 0,
        "min_instances": 1,
        "max_instances": 1,
        "is_turbo_enabled": true,
        "is_cuda_enabled": false,
        "cluster_conf": {
          "cluster_conf_id": 201,
          "cluster_conf_name": "Standard_F16s_v2",
          "machine_type_category": "compute_optimized",
          "machine_type": {
            "machine_type_id": 201,
            "name": "Standard_F16s_v2",
            "vCPUs": 16,
            "memory": "32 GiB",
            "has_cuda": false,
            "gpu_model": null,
            "gpus": 0,
            "gpu_memory": null,
            "cpu_model": [
              "Intel Xeon® Platinum 8168 (SkyLake)"
            ],
            "cpu_min_frequency_GHz": [
              "2.7"
            ],
            "cpu_max_frequency_GHz": [
              "3.7"
            ],
            "has_local_disk": true,
            "local_disk_size_GB": 128,
            "local_num_of_disks": 1,
            "local_disk_throughput_MB": null,
            "has_spot_instance_support": true,
            "machine_price_ycu": 7.2
          },
          "machine_volume_conf": null
        },
        "cloud_env": {
          "cloud_env_id": 3,
          "name": "cloud_env_azure_ui",
          "cloud_provider": {
            "cloud_provider_id": 2,
            "name": "Azure"
          }
        },
        "spark_infra_version": {
          "spark_infra_version_id": 5,
          "spark_docker_image_name": "v3.5.3-2",
          "spark_version": "3.5.3",
          "hive_version": "2.3.9",
          "hadoop_version": "3.2.4",
          "scala_version": "2.12.15",
          "python_version": "3.9.5",
          "notebook_support": true,
          "has_cuda_support": false,
          "thrift_support": true,
          "yeedu_functions_support": true,
          "has_turbo_support": true,
          "turbo_version": "v1.0.6",
          "has_unity_support": true,
          "unity_version": "v1.0.6",
          "has_hive_support": true,
          "cuda_rapids_version": "23.04.1"
        },
        "engine_cluster_spark_config": {
          "max_parallel_spark_job_execution_per_instance": 1,
          "num_of_workers": null
        },
        "metastore_catalog": {
          "metastore_catalog_id": 1,
          "metastore_catalog_name": "metastore_1",
          "description": null,
          "metastore_catalog_type": {
            "metastore_catalog_type_id": 2,
            "name": "DATABRICKS UNITY",
            "description": null
          }
        }
      },
      "thrift_url": "jdbc:hive2://localhost:8080/default;transportMode=http;httpPath=/api/v1/workspace/2/cluster/1/thrift;reuseSameConn=true;maxJobStartTimeout=5;",
      "created_by": {
        "user_id": 6,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 6,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2025-07-14T09:29:41.288317+00:00",
      "from_date": "2025-07-14T09:29:41.288317+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 2
  }
}
```

### search-workspaces

```bash
yeedu cluster search-workspaces -h
```

```bash
usage:  search-workspaces [-h] --cluster_id CLUSTER_ID --workspace_name [WORKSPACE_NAME]
                          [--page_number PAGE_NUMBER] [--limit LIMIT]
                          [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide Cluster Id to list all the associated workspaces.
  --workspace_name [WORKSPACE_NAME]
                        Provide workspace name to search all the workspaces having access
                        to a cluster.
  --page_number PAGE_NUMBER
                        To list Clusters for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of Clusters. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-workspaces example with all the required argument passed.

```bash
yeedu cluster search-workspaces --cluster_id=1 --workspace_name='_jobs' --limit=2
```

- Console output

```bash
{
  "data": [
    {
      "workspace": {
        "workspace_id": 4,
        "name": "stopped_submitted_jobs",
        "description": ""
      },
      "cluster_info": {
        "cluster_id": 1,
        "name": "gcp_test_cluster",
        "cluster_status": "INITIATING",
        "cluster_type": "YEEDU",
        "instance_size": 1,
        "min_instances": 1,
        "max_instances": 1,
        "cluster_conf": {
          "cluster_conf_id": 10,
          "cluster_conf_name": "n1-standard-4",
          "machine_type_category": "general_purpose",
          "machine_type": {
            "machine_type_id": 10,
            "name": "n1-standard-4",
            "vCPUs": 4,
            "memory": "15 GiB",
            "has_cuda": false,
            "gpu_model": null,
            "gpus": 0,
            "gpu_memory": null,
            "cpu_model": [
              "Intel Xeon Scalable (Skylake) 1st Generation",
              "Intel Xeon E5 v4 (Broadwell E5)",
              "Intel Xeon E5 v3 (Haswell)",
              "Intel Xeon E5 v2 (Ivy Bridge)",
              "Intel Xeon E5 (Sandy Bridge)"
            ],
            "cpu_min_frequency_GHz": [
              "2.0",
              "2.2",
              "2.3",
              "2.5",
              "2.6"
            ],
            "cpu_max_frequency_GHz": [
              "3.5",
              "3.7",
              "3.8",
              "3.5",
              "3.6"
            ],
            "has_local_disk": false,
            "local_disk_size_GB": null,
            "local_num_of_disks": null,
            "local_disk_throughput_MB": null,
            "machine_price_ycu": 2.5
          },
          "machine_volume_conf": {
            "volume_conf_id": 2,
            "name": "volume_gcp_2",
            "size": 375,
            "machine_volume_num": 2,
            "machine_volume_strip_num": 2
          }
        },
        "cloud_env": {
          "cloud_env_id": 1,
          "name": "gcp_cloud_env",
          "cloud_provider": {
            "cloud_provider_id": 0,
            "name": "GCP"
          }
        },
        "spark_infra_version": {
          "spark_infra_version_id": 2,
          "spark_docker_image_name": "v3.3.4-3",
          "spark_version": "3.3.4",
          "hive_version": "3.2.3",
          "hadoop_version": "3.2.4",
          "scala_version": "2.12.15",
          "python_version": "3.9.5",
          "notebook_support": true,
          "has_cuda_support": false,
          "thrift_support": true,
          "yeedu_functions_support": true
        },
        "engine_cluster_spark_config": {
          "max_parallel_spark_job_execution_per_instance": 5,
          "num_of_workers": null
        }
      },
      "created_by": {
        "user_id": 6,
        "username": "rt0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 6,
        "username": "rt0000@yeedu.io"
      },
      "last_update_date": "2024-05-31T12:56:02.641984+00:00",
      "from_date": "2024-05-31T12:56:02.641984+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 2
  }
}
```

### list-workspace-clusters

```bash
yeedu cluster list-workspace-clusters -h
```

```bash
usage:  list-workspace-clusters [-h] --workspace_id WORKSPACE_ID
                                [--cluster_status [CLUSTER_STATUS]]
                                [--job_type [{SPARK_JOB,SPARK_SQL,NOTEBOOK,THRIFT_SQL,YEEDU_FUNCTIONS}]]
                                [--page_number PAGE_NUMBER] [--limit LIMIT]
                                [--json-output [{pretty,default}]]
                                [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to list all the associated clusters.
  --cluster_status [CLUSTER_STATUS]
                        Provide Cluster Instance Status from ["INITIATING", "RUNNING",
                        "STOPPING", "STOPPED", "DESTROYING", "DESTROYED", "ERROR",
                        "RESIZING_UP", "RESIZING_DOWN"] to list, For example
                        --cluster_status="RUNNING,DESTROYED".
  --job_type [{SPARK_JOB,SPARK_SQL,NOTEBOOK,THRIFT_SQL,YEEDU_FUNCTIONS}]
                        To list Clusters for a specific job_type.
  --page_number PAGE_NUMBER
                        To list Clusters for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of Clusters. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-workspace-clusters example with all the required arguments passed.

```bash
yeedu cluster list-workspace-clusters --workspace_id=1
```

- Console output

```bash
{
  "data": [
    {
      "workspace": {
        "workspace_id": 1,
        "name": "notebook_workspace",
        "description": ""
      },
      "cluster_info": {
        "cluster_id": 1,
        "name": "gcp_test_cluster",
        "cluster_status": "INITIATING",
        "cluster_type": "YEEDU",
        "instance_size": 1,
        "min_instances": 1,
        "max_instances": 1,
        "cluster_conf": {
          "cluster_conf_id": 10,
          "cluster_conf_name": "n1-standard-4",
          "machine_type_category": "general_purpose",
          "machine_type": {
            "machine_type_id": 10,
            "name": "n1-standard-4",
            "vCPUs": 4,
            "memory": "15 GiB",
            "has_cuda": false,
            "gpu_model": null,
            "gpus": 0,
            "gpu_memory": null,
            "cpu_model": [
              "Intel Xeon Scalable (Skylake) 1st Generation",
              "Intel Xeon E5 v4 (Broadwell E5)",
              "Intel Xeon E5 v3 (Haswell)",
              "Intel Xeon E5 v2 (Ivy Bridge)",
              "Intel Xeon E5 (Sandy Bridge)"
            ],
            "cpu_min_frequency_GHz": [
              "2.0",
              "2.2",
              "2.3",
              "2.5",
              "2.6"
            ],
            "cpu_max_frequency_GHz": [
              "3.5",
              "3.7",
              "3.8",
              "3.5",
              "3.6"
            ],
            "has_local_disk": false,
            "local_disk_size_GB": null,
            "local_num_of_disks": null,
            "local_disk_throughput_MB": null,
            "machine_price_ycu": 2.5
          },
          "machine_volume_conf": {
            "volume_conf_id": 2,
            "name": "volume_gcp_2",
            "size": 375,
            "machine_volume_num": 2,
            "machine_volume_strip_num": 2
          }
        },
        "cloud_env": {
          "cloud_env_id": 1,
          "name": "gcp_cloud_env",
          "cloud_provider": {
            "cloud_provider_id": 0,
            "name": "GCP"
          }
        },
        "spark_infra_version": {
          "spark_infra_version_id": 2,
          "spark_docker_image_name": "v3.3.4-3",
          "spark_version": "3.3.4",
          "hive_version": "3.2.3",
          "hadoop_version": "3.2.4",
          "scala_version": "2.12.15",
          "python_version": "3.9.5",
          "notebook_support": true,
          "has_cuda_support": false,
          "thrift_support": true,
          "yeedu_functions_support": true
        },
        "engine_cluster_spark_config": {
          "max_parallel_spark_job_execution_per_instance": 5,
          "num_of_workers": null
        }
      },
      "created_by": {
        "user_id": 3,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 3,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2024-06-07T10:51:22.247082+00:00",
      "from_date": "2024-06-07T10:51:22.247082+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-workspace-clusters

```bash
yeedu cluster search-workspace-clusters -h
```

```bash
usage:  search-workspace-clusters [-h] --workspace_id WORKSPACE_ID
                                  [--cluster_name [CLUSTER_NAME]]
                                  [--cluster_status [CLUSTER_STATUS]]
                                  [--job_type [{SPARK_JOB,SPARK_SQL,NOTEBOOK,THRIFT_SQL,YEEDU_FUNCTIONS}]]
                                  [--page_number PAGE_NUMBER] [--limit LIMIT]
                                  [--json-output [{pretty,default}]]
                                  [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to search all the associated clusters.
  --cluster_name [CLUSTER_NAME]
                        Provide cluster name to search all the associated workspace
                        clusters.
  --cluster_status [CLUSTER_STATUS]
                        Provide cluster instance status from ["INITIATING", "RUNNING",
                        "STOPPING", "STOPPED", "DESTROYING", "DESTROYED", "ERROR",
                        "RESIZING_UP", "RESIZING_DOWN"] to search, for example
                        --cluster_status="RUNNING,DESTROYED".
  --job_type [{SPARK_JOB,SPARK_SQL,NOTEBOOK,THRIFT_SQL,YEEDU_FUNCTIONS}]
                        To search clusters of a specific job_type.
  --page_number PAGE_NUMBER
                        To search clusters for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of clusters. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-confs example with required argument '--cluster_conf_name' passed.

```bash
yeedu cluster search-workspace-clusters --workspace_id=1 --cluster_name="yeedu_"
```

- Console output

```bash
{
  "data": [
    {
      "workspace": {
        "workspace_id": 1,
        "name": "notebook_workspace",
        "description": ""
      },
      "cluster_info": {
        "cluster_id": 1,
        "name": "gcp_test_cluster",
        "cluster_status": "INITIATING",
        "cluster_type": "YEEDU",
        "instance_size": 1,
        "min_instances": 1,
        "max_instances": 1,
        "cluster_conf": {
          "cluster_conf_id": 10,
          "cluster_conf_name": "n1-standard-4",
          "machine_type_category": "general_purpose",
          "machine_type": {
            "machine_type_id": 10,
            "name": "n1-standard-4",
            "vCPUs": 4,
            "memory": "15 GiB",
            "has_cuda": false,
            "gpu_model": null,
            "gpus": 0,
            "gpu_memory": null,
            "cpu_model": [
              "Intel Xeon Scalable (Skylake) 1st Generation",
              "Intel Xeon E5 v4 (Broadwell E5)",
              "Intel Xeon E5 v3 (Haswell)",
              "Intel Xeon E5 v2 (Ivy Bridge)",
              "Intel Xeon E5 (Sandy Bridge)"
            ],
            "cpu_min_frequency_GHz": [
              "2.0",
              "2.2",
              "2.3",
              "2.5",
              "2.6"
            ],
            "cpu_max_frequency_GHz": [
              "3.5",
              "3.7",
              "3.8",
              "3.5",
              "3.6"
            ],
            "has_local_disk": false,
            "local_disk_size_GB": null,
            "local_num_of_disks": null,
            "local_disk_throughput_MB": null,
            "machine_price_ycu": 2.5
          },
          "machine_volume_conf": {
            "volume_conf_id": 2,
            "name": "volume_gcp_2",
            "size": 375,
            "machine_volume_num": 2,
            "machine_volume_strip_num": 2
          }
        },
        "cloud_env": {
          "cloud_env_id": 1,
          "name": "gcp_cloud_env",
          "cloud_provider": {
            "cloud_provider_id": 0,
            "name": "GCP"
          }
        },
        "spark_infra_version": {
          "spark_infra_version_id": 2,
          "spark_docker_image_name": "v3.3.4-3",
          "spark_version": "3.3.4",
          "hive_version": "3.2.3",
          "hadoop_version": "3.2.4",
          "scala_version": "2.12.15",
          "python_version": "3.9.5",
          "notebook_support": true,
          "has_cuda_support": false,
          "thrift_support": true,
          "yeedu_functions_support": true
        },
        "engine_cluster_spark_config": {
          "max_parallel_spark_job_execution_per_instance": 5,
          "num_of_workers": null
        }
      },
      "created_by": {
        "user_id": 3,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 3,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2024-06-07T10:51:22.247082+00:00",
      "from_date": "2024-06-07T10:51:22.247082+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

# Workspace

| Command Name        | Utility                                 |
| ------------------- | --------------------------------------- |
| [create](#create-1) | Create a new workspace.                 |
| [list](#list-1)     | List all available workspaces.          |
| [search](#search-1) | Search for workspaces by name.          |
| [get](#get-1)       | Get details of a specific workspace.    |
| [edit](#edit-1)     | Modify details of a specific workspace. |
| [enable](#enable)   | Enable a specific workspace.            |
| [disable](#disable) | Disable a specific workspace.           |
| [export](#export)   | Export a specific workspace.            |
| [import](#import)   | Import a specific workspace.            |

### create

```bash
yeedu workspace create -h
```

```bash
usage:  create [-h] [--name NAME] [--description DESCRIPTION]
               [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name NAME           Provide name to create workspace.
  --description DESCRIPTION
                        Provide description to create workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create example with all the required arguments passed.

```bash
yeedu workspace create --name="spark_jobs_test" --description="Test Spark Jobs"
```

- Console output

```bash
{
  "workspace_id": "1",
  "name": "spark_jobs_test",
  "description": "Test Spark Jobs",
  "tenant_id": "59608f6e-cb14-4687-98dc-e0f80e608f05",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-13T09:50:32.306Z",
  "from_date": "2024-06-13T09:50:32.306Z",
  "to_date": null
}
```

### list

```bash
  yeedu workspace list -h
```

```bash
usage:  list [-h] [--enable [{true,false}]] [--page_number PAGE_NUMBER] [--limit LIMIT]
             [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --enable [{true,false}]
                        Provide enable as true or false to list Workspaces.
  --page_number PAGE_NUMBER
                        To list Workspaces for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of Workspaces. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list example with optional arguments passed.

```bash
yeedu workspace list --limit=1 --page_number=1
```

- Console output

```bash
{
  "data": [
    {
      "workspace_id": 3,
      "name": "spark_jobs_test",
      "job_count": 0,
      "notebook_count": 0,
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "tenant_id": "59608f6e-cb14-4687-98dc-e0f80e608f05",
      "last_update_date": "2024-06-13T09:50:32.306341+00:00",
      "from_date": "2024-06-13T09:50:32.306341+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 3,
    "total_pages": 3,
    "limit": 1,
    "next_page": 2
  }
}
```

### search

```bash
yeedu workspace search -h
```

```bash
usage:  search [-h] --workspace_name WORKSPACE_NAME
               [--enable [{true,false}]] [--page_number PAGE_NUMBER]
               [--limit LIMIT] [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_name WORKSPACE_NAME
                        Provide workspace name to search workspaces.
  --enable [{true,false}]
                        Provide enable as true or false to search workspaces.
  --page_number PAGE_NUMBER
                        To search workspaces for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of workspaces. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search example with the required argument passed.

```bash
yeedu workspace search --workspace_name="spark_"
```

- Console output

```bash
{
  "data": [
    {
      "workspace_id": 3,
      "name": "spark_jobs_test",
      "job_count": 0,
      "notebook_count": 0,
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "tenant_id": "59608f6e-cb14-4687-98dc-e0f80e608f05",
      "last_update_date": "2024-06-13T09:50:32.306341+00:00",
      "from_date": "2024-06-13T09:50:32.306341+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get

```bash
yeedu workspace get -h
```

```bash
usage:  get [-h] [--workspace_id WORKSPACE_ID]
            [--workspace_name WORKSPACE_NAME]
            [--json-output [{pretty,default}]]
            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to get information about a specific Workspace.
  --workspace_name WORKSPACE_NAME
                        Provide workspace_name to get information about a specific Workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get example with any one of the required argument passed.

```bash
yeedu workspace get --workspace_id=1
```

- Console output

```bash
{
  "workspace_id": 3,
  "name": "spark_jobs_test",
  "description": "Test Spark Jobs",
  "created_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "tenant_id": "59608f6e-cb14-4687-98dc-e0f80e608f05",
  "last_update_date": "2024-06-13T09:50:32.306341+00:00",
  "from_date": "2024-06-13T09:50:32.306341+00:00",
  "to_date": "infinity"
}
```

### get-stats

```bash
yeedu workspace get-stats -h
```

```bash
usage:  get-stats [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME]
                  [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Specifies the ID of the workspace to retrieve stats.
  --workspace_name WORKSPACE_NAME
                        Specifies the name of the workspace to retrieve stats.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- get-stats example with any one of the required argument passed.

```bash
yeedu workspace get-stats --workspace_id=1
```

- Console output

```bash
{
  "SUBMITTED": 1,
  "RUNNING": 2,
  "DONE": 4,
  "ERROR": 0,
  "TERMINATED": 0,
  "STOPPING": 1,
  "STOPPED": 1,
  "TOTAL_JOB_COUNT": 9
}
```

### edit

```bash
yeedu workspace edit -h
```

```bash
usage:  edit [-h] [--workspace_id WORKSPACE_ID]
             [--workspace_name WORKSPACE_NAME] [--name NAME]
             [--description DESCRIPTION]
             [--json-output [{pretty,default}]]
             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to edit a specific Workspace.
  --workspace_name WORKSPACE_NAME
                        Provide workspace_name to edit a specific Workspace.
  --name NAME           Provide name to edit a specific Workspace.
  --description DESCRIPTION
                        Provide description to edit a specific Workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- edit example with any one of the required argument '--workspace_id' and other optional argument is passed which is to be updated.

```bash
yeedu workspace edit --workspace_id=1 --description="Test Spark Curation Jobs"
```

- Console output

```bash
{
  "workspace_id": "1",
  "name": "spark_jobs_test",
  "description": "Test Spark Curation Jobs",
  "tenant_id": "59608f6e-cb14-4687-98dc-e0f80e608f05",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-13T10:12:51.975Z",
  "from_date": "2024-06-13T09:50:32.306Z",
  "to_date": null
}
```

### enable

```bash
yeedu workspace enable -h
```

```bash
usage:  enable [-h] [--workspace_id WORKSPACE_ID]
               [--workspace_name WORKSPACE_NAME]
               [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to enable a specific Workspace.
  --workspace_name WORKSPACE_NAME
                        Provide workspace_name to enable a specific Workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- enable example with any one of the required argument passed.

```bash
yeedu workspace enable --workspace_id=1
```

- Console output

```bash
{
  "workspace_id": "1",
  "name": "spark_jobs_test",
  "description": "Test Spark Curation Jobs",
  "tenant_id": "59608f6e-cb14-4687-98dc-e0f80e608f05",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-13T10:15:13.222Z",
  "from_date": "2024-06-13T09:50:32.306Z",
  "to_date": null
}
```

### disable

```bash
yeedu workspace disable -h
```

```bash
usage:  disable [-h] [--workspace_id WORKSPACE_ID]
                [--workspace_name WORKSPACE_NAME]
                [--json-output [{pretty,default}]]
                [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to disable a specific Workspace.
  --workspace_name WORKSPACE_NAME
                        Provide workspace_name to disable a specific Workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- disable example with any one of the required argument passed.

```bash
yeedu workspace disable --workspace_id=1
```

- Console output

```bash
{
  "workspace_id": "1",
  "name": "spark_jobs_test",
  "description": "Test Spark Curation Jobs",
  "tenant_id": "59608f6e-cb14-4687-98dc-e0f80e608f05",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-13T10:14:43.906Z",
  "from_date": "2024-06-13T09:50:32.306Z",
  "to_date": "2024-06-13T10:14:43.906Z"
}
```

### export

```bash
yeedu workspace export -h
```

```bash
usage:  export [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME]
               [--enable [{true,false}]] [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to export a specific workspace.
  --workspace_name WORKSPACE_NAME
                        Provide workspace name to export a specific workspace.
  --enable [{true,false}]
                        Provide enable to export active job and notebooks
                        of a specific workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- export example with any one of the required argument passed.

```bash
yeedu workspace export --workspace_id=1
```

- Console output

```bash
{
  "jobs": [
    {
      "name": "yeedu_test_job",
      "spark_job_type": {
        "job_type": "SPARK_JOB",
        "language": "Jar"
      },
      "cluster_info": {
        "cluster_name": "aws_test_cluster",
        "cluster_type": "YEEDU"
      },
      "max_concurrency": 0,
      "files": [],
      "properties_file": null,
      "conf": [],
      "packages": [],
      "repositories": [],
      "jars": [],
      "archives": [],
      "driver_memory": null,
      "driver_java_options": "-Dderby.system.home=/yeedu/spark_metastores/1721298078-74183",
      "driver_library_path": null,
      "driver_class_path": null,
      "executor_memory": null,
      "principal": null,
      "keytab": null,
      "queue": null,
      "job_class_name": "org.apache.spark.examples.SparkPi",
      "job_command": "/opt/spark/examples/jars/spark-examples_2.12-3.2.2.jar",
      "job_arguments": "10000",
      "job_rawScalaCode": null,
      "job_timeout_min": 5,
      "driver_cores": null,
      "total_executor_cores": null,
      "executor_cores": null,
      "num_executors": null,
      "should_append_params": false
    },
    .....
    {
      "name": "yeedu_test_job_n",
      "spark_job_type": {
        "job_type": "SPARK_JOB",
        "language": "Jar"
      },
      "cluster_info": {
        "cluster_name": "yeedu_cluster_instance",
        "cluster_type": "YEEDU"
      },
      "max_concurrency": 0,
      "files": [],
      "properties_file": null,
      "conf": [],
      "packages": [],
      "repositories": [],
      "jars": [],
      "archives": [],
      "driver_memory": null,
      "driver_java_options": null,
      "driver_library_path": null,
      "driver_class_path": null,
      "executor_memory": null,
      "principal": null,
      "keytab": null,
      "queue": null,
      "job_class_name": "org.apache.spark.examples.SparkPi",
      "job_command": "/opt/spark/examples/jars/spark-examples_2.12-3.2.2.jar",
      "job_arguments": "10",
      "job_rawScalaCode": null,
      "job_timeout_min": null,
      "driver_cores": null,
      "total_executor_cores": null,
      "executor_cores": null,
      "num_executors": null,
      "should_append_params": false
    }
  ],
  "notebooks": [
    {
      "name": "test_notebook_1",
      "spark_job_type": {
        "job_type": "NOTEBOOK",
        "language": "Python3"
      },
      "cluster_info": {
        "cluster_name": "gcp_cluster",
        "cluster_type": "YEEDU"
      },
      "notebook_cells": {
        "cells": [
          {
            "code": "print(\"hello\")",
            "cell_uuid": "f98e6834-09e2-4c59-84d6-130769c9d182"
          }
        ]
      },
      "conf": [],
      "packages": [],
      "jars": [],
      "files": [],
      "driver_memory": null,
      "executor_memory": null,
      "driver_cores": null,
      "total_executor_cores": null,
      "executor_cores": null,
      "num_executors": null,
      "should_append_params": false
    },
    ......
    {
      "name": "test_notebook_n",
      "spark_job_type": {
        "job_type": "NOTEBOOK",
        "language": "Python3"
      },
      "cluster_info": null,
      "notebook_cells": {
        "cells": [
          {
            "code": "",
            "cell_uuid": "a894a53f-391a-4c10-8f4f-6ea72ae1f1af"
          }
        ]
      },
      "conf": [],
      "packages": [],
      "jars": [],
      "files": [],
      "driver_memory": null,
      "executor_memory": null,
      "driver_cores": null,
      "total_executor_cores": null,
      "executor_cores": null,
      "num_executors": null,
      "should_append_params": false
    }
  ]
}
```

### import

```bash
yeedu workspace import -h
```

```bash
usage:  import [-h] [--workspace_id WORKSPACE_ID]
               [--workspace_name WORKSPACE_NAME]
               [--cluster_id CLUSTER_ID] [--cluster_name CLUSTER_NAME]
               [--permissive [{true,false}]]
               [--overwrite [{true,false}]] --file_path FILE_PATH
               [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to import a specific
                        workspace to it.
  --workspace_name WORKSPACE_NAME
                        Provide workspace name to import a specific
                        workspace.
  --cluster_id CLUSTER_ID
                        Provide cluster instance id to attach with job
                        configurations in the workspace to be
                        imported.
  --cluster_name CLUSTER_NAME
                        Provide cluster instance name to attach with
                        jobs in the workspace to be
                        imported.
  --permissive [{true,false}]
                        Provide permissive option for partial imports
                        when encountering errors. (default: false)
  --overwrite [{true,false}]
                        Provide overwrite option to override any
                        existsing workspace. (default: false)
  --file_path FILE_PATH
                        Provide file path from where a specific
                        workspace is to be imported.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set
                        to 'true'. (default: false)
```

- import example with any one of the required argument passed.

```bash
yeedu workspace import --workspace_id=1 --file_path='/home/user/workspace.yeedu'
```

- Console output

```bash
{
  "message": "All jobs were successfully imported. All notebooks were successfully imported.",
  "job_details": {
    "successful_imports": [
      {
        "message": "The job: 'yeedu_test_job' of type: 'SPARK_JOB' is overwritten and imported successfully.",
        "warnings": [
          "The file path specified in 'job_command': '/opt/spark/examples/jars/spark-examples_2.12-3.2.2.jar' does not exist in the object storage manager of cluster ID: 13."
        ]
      },
      .....
      {
        "message": "The job: 'yeedu_test_job_n' of type: 'SPARK_JOB' is overwritten and imported successfully."
      }
    ]
  },
  "notebook_details": {
    "successful_imports": [
      {
        "message": "The notebook: 'yeedu_test_notebook' of type: 'NOTEBOOK' is overwritten and imported successfully.",
        "warnings": [
          "The cluster was not attached, and Spark parameters were ignored because the cluster name: 'gcp_cluster' was not found or has been destroyed."
        ]
      },
      ....
      {
        "message": "The notebook: 'yeedu_test_notebook_n' of type: 'NOTEBOOK' is overwritten and imported successfully.",
        "warnings": [
          "The cluster was not attached, and Spark parameters were ignored because no cluster was provided."
        ]
      }
    ]
  }
}
```
## Workspace Files

| Command Name                                            | Utility                                             |
| ------------------------------------------------------- | --------------------------------------------------- |
| [create-workspace-file](#create-workspace-files)        | To create a Workspace File.                         |
| [list-workspace-files](#list-workspace-files)           | To list all the available Workspace Files.          |
| [search-workspace-files](#search-workspace-files)       | To search all the available Workspace Files.        |
| [get-workspace-file](#get-workspace-file)               | To get information about a specific Workspace File. |
| [delete-workspace-file](#delete-workspace-file)         | To delete a specific Workspace File.                |
| [download-workspace-file](#download-workspace-file)     | Download file for a specific workspace.             |
| [rename-workspace-file](#rename-workspace-file)         | Rename file/directory for a specific workspace.     |
| [get-workspace-files-usage](#get-workspace-files-usage) | To get workspace files usage details for a specific workspace. |
| [move-workspace-file](#move-workspace-file)             | Move workspace file for a one directory to another directory. |
| [copy-workspace-file](#copy-workspace-file)             | Copy workspace file for a one directory to another directory. |


### create-workspace-files

```bash
  yeedu workspace create-workspace-files -h
```

```bash
usage:  create-workspace-file [-h] [--workspace_id WORKSPACE_ID]
                              [--workspace_name WORKSPACE_NAME]
                              --local_file_path LOCAL_FILE_PATH
                              [--overwrite [{true,false}]]
                              [--recursive [{true,false}]]
                              [--root_output_dir [ROOT_OUTPUT_DIR]]
                              [--json-output [{pretty,default}]]
                              [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to create-workspace-file.
  --workspace_name WORKSPACE_NAME
                        Provide Workspace Name to to create-workspace-
                        file.
  --local_file_path LOCAL_FILE_PATH
                        Provide local_file_path to create-workspace-
                        file.
  --overwrite [{true,false}]
                        Provide overwrite to create-workspace-file.
                        (default: false)
  --recursive [{true,false}]
                        Provide recursive to create-workspace-file.
                        (default: false)
  --root_output_dir [ROOT_OUTPUT_DIR]
                        Provide root_output_dir to create-workspace-
                        file.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set
                        to 'true'. (default: false)
```

- create example with all the required arguments passed.

```bash
yeedu workspace create-workspace-file --workspace_id 9 --local_file_path ~/script_warm_start --root_output_dir /test/p
```

- Console output

```bash
{
  "workspace_file_id": "208",
  "workspace_id": "9",
  "file_name": "script_warm_start",
  "full_file_path": "file:///files/test/p/script_warm_start",
  "file_size_bytes": "503",
  "file_type": "",
  "is_dir": false,
  "parent_id": "207",
  "tenant_id": "8cee6100-7086-4138-92fd-712046174e91",
  "created_by_user_id": "32",
  "modified_by_user_id": "32",
  "last_update_date": "2025-01-13T15:12:05.592Z",
  "from_date": "2025-01-13T15:12:05.592Z",
  "to_date": null
}
```

### list-workspace-files

```bash
  yeedu workspace list-workspace-files -h
```

```bash
usage:  list-workspace-files [-h] [--workspace_id WORKSPACE_ID]
                             [--workspace_name WORKSPACE_NAME]
                             [--file_id FILE_ID]
                             [--file_path FILE_PATH]
                             [--recursive [{true,false}]]
                             [--page_number PAGE_NUMBER]
                             [--limit LIMIT]
                             [--json-output [{pretty,default}]]
                             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to list all the
                        available Workspace Files.
  --workspace_name WORKSPACE_NAME
                        Provide Workspace Name to list all the
                        available Workspace Files.
  --file_id FILE_ID     Provide Workspace File Id to list all the
                        available Files.
  --file_path FILE_PATH
                        Provide Workspace File Path to list all the
                        available Files.
  --recursive [{true,false}]
                        Provide recursive to list files recursively.
                        (default: false)
  --page_number PAGE_NUMBER
                        To list Workspace Files for a specific
                        page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of Workspace
                        Files. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output.
                        (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if
                        set to 'true'. (default: false)
```

- list example with optional arguments passed.

```bash
yeedu workspace list-workspace-files --workspace_id 9 --limit 1
```

- Console output

```bash
{
  "data": [
    {
      "workspace_file_id": 205,
      "workspace": {
        "workspace_id": 9,
        "workspace_name": "test_workspace_1",
        "description": null
      },
      "file_name": "predict_weather",
      "full_file_path": "file:///files/predict_weather",
      "file_size_bytes": "0",
      "file_type": "",
      "is_dir": false,
      "parent_id": null,
      "notebook_info": {
        "notebook_id": null,
        "notebook_type": null
      },
      "tenant_id": "8cee6100-7086-4138-92fd-712046174e91",
      "created_by": {
        "user_id": 34,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 34,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2025-01-08T07:17:10.798226+00:00",
      "from_date": "2025-01-08T07:17:10.798226+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 1
  }
}
```

### search-workspace-files

```bash
yeedu workspace search-workspace-files -h
```

```bash
usage:  search-workspace-files [-h] --file_name FILE_NAME
                               [--workspace_id WORKSPACE_ID]
                               [--workspace_name WORKSPACE_NAME]
                               [--file_id FILE_ID]
                               [--file_path FILE_PATH]
                               [--recursive [{true,false}]]
                               [--page_number PAGE_NUMBER]
                               [--limit LIMIT]
                               [--json-output [{pretty,default}]]
                               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --file_name FILE_NAME
                        Provide File Name to search all the available
                        Workspace Files.
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to search all the available
                        Workspace Files.
  --workspace_name WORKSPACE_NAME
                        Provide Workspace Name to search all the
                        available Workspace Files.
  --file_id FILE_ID     Provide Workspace File Id to search all the
                        available Files.
  --file_path FILE_PATH
                        Provide Workspace File Path to search all the
                        available Files.
  --recursive [{true,false}]
                        Provide recursive to search files recursively.
                        (default: false)
  --page_number PAGE_NUMBER
                        To search Workspace Files for a specific
                        page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of Workspace
                        Files. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to
                        'true'. (default: false)
```

- search example with the required argument passed.

```bash
yeedu workspace search-workspace-files --file_name predict_weather --workspace_id 9 --limit 1
```

- Console output

```bash
{
  "data": [
    {
      "workspace_file_id": 205,
      "workspace": {
        "workspace_id": 9,
        "workspace_name": "test_workspace_1",
        "description": null
      },
      "file_name": "predict_weather",
      "full_file_path": "file:///files/predict_weather",
      "file_size_bytes": "0",
      "file_type": "",
      "is_dir": false,
      "parent_id": null,
      "notebook_info": {
        "notebook_id": null,
        "notebook_type": null
      },
      "tenant_id": "8cee6100-7086-4138-92fd-712046174e91",
      "created_by": {
        "user_id": 34,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 34,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2025-01-08T07:17:10.798226+00:00",
      "from_date": "2025-01-08T07:17:10.798226+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 1
  }
}
```

### get-workspace-file

```bash
yeedu workspace get-workspace-file -h
```

```bash
usage:  get-workspace-file [-h] [--workspace_id WORKSPACE_ID]
                           [--workspace_name WORKSPACE_NAME]
                           [--file_id FILE_ID] [--file_path FILE_PATH]
                           [--json-output [{pretty,default}]]
                           [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to get information about a
                        specific Workspace Files.
  --workspace_name WORKSPACE_NAME
                        Provide Workspace Name to get information about a
                        specific Workspace Files.
  --file_id FILE_ID     Provide File Id to get information about a specific
                        Workspace Files.
  --file_path FILE_PATH
                        Provide File Path to get information about a
                        specific Workspace Files.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to
                        'true'. (default: false)

```

- get example with any one of the required argument passed.

```bash
yeedu workspace get-workspace-file --workspace_id 9 --file_id 205
```

- Console output

```bash
{
  "workspace_file_id": 205,
  "workspace": {
    "workspace_id": 9,
    "workspace_name": "test_workspace_1",
    "description": null
  },
  "file_name": "predict_weather",
  "full_file_path": "file:///files/predict_weather",
  "file_size_bytes": "0",
  "file_type": "",
  "is_dir": false,
  "parent_id": null,
  "notebook_info": {
        "notebook_id": null,
        "notebook_type": null
      },
  "tenant_id": "8cee6100-7086-4138-92fd-712046174e91",
  "created_by": {
    "user_id": 34,
    "username": "ysu0000@yeedu.io"
  },
  "modified_by": {
    "user_id": 34,
    "username": "ysu0000@yeedu.io"
  },
  "last_update_date": "2025-01-08T07:17:10.798226+00:00",
  "from_date": "2025-01-08T07:17:10.798226+00:00",
  "to_date": "infinity"
}
```

### delete-workspace-file

```bash
 yeedu workspace delete-workspace-file -h
```

```bash
usage:  delete-workspace-file [-h] [--workspace_id WORKSPACE_ID]
                              [--workspace_name WORKSPACE_NAME]
                              [--file_id FILE_ID]
                              [--file_path FILE_PATH]
                              [--json-output [{pretty,default}]]
                              [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to delete a specific
                        Workspace File.
  --workspace_name WORKSPACE_NAME
                        Provide Workspace Name to delete a specific
                        Workspace File.
  --file_id FILE_ID     Provide File Id to delete a specific Workspace
                        Files.
  --file_path FILE_PATH
                        Provide File Path to delete a specific Workspace
                        Files.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set
                        to 'true'. (default: false)

```

- delete-workspace-file example with any one of the required arguments passed.

```bash
yeedu workspace delete-workspace-file --workspace_id 9 --file_id 208
```

- Console output

```bash
{
  "message": "The File: 'file:///files/test/p/script_warm_start' has been deleted."
}
```

### download-workspace-file

```bash
yeedu workspace download-workspace-file -h
```

```bash
usage:  download-workspace-file [-h] [--workspace_id WORKSPACE_ID]
                                [--workspace_name WORKSPACE_NAME]
                                [--file_id FILE_ID] [--file_path FILE_PATH]
                                [--json-output [{pretty,default}]]
                                [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to download file.
  --workspace_name WORKSPACE_NAME
                        Provide Workspace Name to download file.
  --file_id FILE_ID     Provide File Id of the file to be downloaded.
  --file_path FILE_PATH
                        Provide File Path of the file to be downloaded.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to
                        'true'. (default: false)
```

- download-workspace-file example with any one of the required arguments passed.

```bash
yeedu workspace download-workspace-file --workspace_id 9 --file_id 208
```

- Console output

```bash
{
  "message": "File : script_warm_start saved successfully"
}
```

### rename-workspace-file

```bash
yeedu workspace rename-workspace-file -h
```

```bash
usage:  rename-workspace-file [-h] [--workspace_id WORKSPACE_ID]
                                [--workspace_name WORKSPACE_NAME]
                                [--file_id FILE_ID]
                                [--file_path FILE_PATH] [--file_name FILE_NAME]
                                [--json-output [{pretty,default}]]
                                [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to rename a file.
  --workspace_name WORKSPACE_NAME
                        Provide Workspace Name to rename a file.
  --file_id FILE_ID
                        Provide File ID of the file to be renamed.
  --file_path FILE_PATH
                        Provide File Path of the file to be renamed.
  --file_name FILE_NAME
                        Provide the new file name.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to
                        'true'. (default: false)
```

- rename-workspace-file example with any one of the required arguments passed.

```bash
yeedu workspace rename-workspace-file --workspace_id 1 --file_path /foo/bar/file1.txt --file_name file2.txt
```

- Console output

```bash
{
  "message": "'/workspaces/1/foo/bar/file1.txt' has been renamed to '/workspaces/1/foo/bar/file2.txt'"
}
```

### get-workspace-files-usage

```bash
yeedu workspace get-workspace-files-usage -h
```

```bash
options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to get workspace files usage details for Workspace.
  --workspace_name WORKSPACE_NAME
                        Provide Workspace Name to get workspace files usage details for Workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get example with any one of the required argument passed.

```bash
yeedu workspace get-workspace-files-usage --workspace_id 1
```

- Console output

```bash
{
  "workspace_id": "1",
  "workspace_name": "ui_team_workspace",
  "workspace_files_usage_in_bytes": 4675074499.19,
  "workspace_files_available_usage_in_bytes": 49012016700.81,
  "workspace_files_maximum_allowed_usage_in_bytes": 53687091200,
  "workspace_files_uploaded": 1769,
  "workspace_files_maximum_upload_limit": 10000
}
```

### move-workspace-file

```bash
yeedu workspace move-workspace-file -h
```

```bash
yeedu workspace move-workspace-file -h
usage:  move-workspace-file [-h] [--workspace_id WORKSPACE_ID]
                            [--workspace_name WORKSPACE_NAME]
                            [--source_file_id SOURCE_FILE_ID]
                            [--source_file_path SOURCE_FILE_PATH]
                            --destination_file_path
                            DESTINATION_FILE_PATH
                            [--overwrite [{true,false}]]
                            [--json-output [{pretty,default}]]
                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to Move Workspace
                        file.
  --workspace_name WORKSPACE_NAME
                        Provide Workspace Name to Move Workspace
                        file.
  --source_file_id SOURCE_FILE_ID
                        Provide Source File Id to Move a specific
                        Workspace File.
  --source_file_path SOURCE_FILE_PATH
                        Provide Source File Path of the file to
                        Move Workspace File.
  --destination_file_path DESTINATION_FILE_PATH
                        Provide Destination File Path to Move
                        Workspace File.
  --overwrite [{true,false}]
                        Provide Overwrite to Move Workspace File.
                        (default: false)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output.
                        (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if
                        set to 'true'. (default: false)
```

- move-workspace-file example with any one of the required arguments passed.

```bash
yeedu workspace move-workspace-file --workspace_id 1 --source_file_path /dest/sub/file_3.txt --destination_file_path /source/sub/sub --overwrite true
```

- Console output

```bash
{
  "message": "Moved /dest/sub/file_3.txt to /source/sub/sub in Workspace Id: 1"
}
```

### copy-workspace-file

```bash
yeedu workspace copy-workspace-file -h
```

```bash
 yeedu workspace copy-workspace-file -h
usage:  copy-workspace-file [-h] [--workspace_id WORKSPACE_ID]
                            [--workspace_name WORKSPACE_NAME]
                            [--source_file_id SOURCE_FILE_ID]
                            [--source_file_path SOURCE_FILE_PATH]
                            --destination_file_path
                            DESTINATION_FILE_PATH
                            [--overwrite [{true,false}]]
                            [--json-output [{pretty,default}]]
                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to Copy Workspace
                        File.
  --workspace_name WORKSPACE_NAME
                        Provide Workspace Name to Copy Workspace
                        File.
  --source_file_id SOURCE_FILE_ID
                        Provide Source File Id to Copy a
                        specific Workspace File.
  --source_file_path SOURCE_FILE_PATH
                        Provide Source File Path of the
                        Workspace File to Copy.
  --destination_file_path DESTINATION_FILE_PATH
                        Provide Destination File Path to Copy
                        Workspace File.
  --overwrite [{true,false}]
                        Provide Overwrite to Copy Workspace
                        File. (default: false)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output.
                        (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format
                        if set to 'true'. (default: false)
```

- copy-workspace-file example with any one of the required arguments passed.

```bash
yeedu workspace copy-workspace-file --workspace_id 1 --source_file_path /source/sub/sub/file_3.txt --destination_file_path /dest/sub
```

- Console output

```bash
{
  "message": "Copied /source/sub/sub/file_3.txt to /dest/sub in Workspace Id: 1"
}
```

## Workspace Access Control

| Command Name                                  | Utility                                                                           |
| --------------------------------------------- | --------------------------------------------------------------------------------- |
| [create-user-access](#create-user-access)     | Assign access to a user on a specific workspace                                   |
| [create-group-access](#create-group-access)   | Assign access to a group on a specific workspace                                  |
| [delete-user-access](#delete-user-access)     | Delete access of a user on a specific workspace                                   |
| [delete-group-access](#delete-group-access)   | Delete access of a group on a specific workspace                                  |
| [list-users](#list-users)                     | To list users who have no permissions in a workspace.                             |
| [search-users](#search-users)                 | To search for users by username who have no permissions in a workspace.           |
| [match-user](#match-user)                     | To match the exact username having access to a workspace.                         |
| [list-groups](#list-groups)                   | To list groups who have no permissions in a workspace.                            |
| [search-groups](#search-groups)               | To search for groups by groupname who have no permissions in a workspace.         |
| [match-group](#match-group)                   | To match the exact groupname having access to a workspace.                        |
| [get-user-access](#get-user-access)           | To get the permission of the user having access to a workspace.                   |
| [get-group-access](#get-group-access)         | To get the permission of the group having access to a workspace.                  |
| [list-users-access](#list-users-access)       | To list all the permissions of the users having access to a workspace.            |
| [search-users-access](#search-users-access)   | To search all the users for the provided username having access to a workspace.   |
| [list-groups-access](#list-groups-access)     | To list all the permissions of the groups having access to a workspace.           |
| [search-groups-access](#search-groups-access) | To search all the groups for the provided groupname having access to a workspace. |

### create-user-access

```bash
  yeedu workspace create-user-access -h
```

```bash
usage:  create-user-access [-h] --workspace_id WORKSPACE_ID --user_id
                           USER_ID --permission_id PERMISSION_ID
                           [--json-output [{pretty,default}]]
                           [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to assign user access on a workspace.
  --user_id USER_ID     Provide User Id to assign user access on a workspace.
  --permission_id PERMISSION_ID
                        Provide Permission Id to assign user access on a workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-user-access example with all the required arguments passed.

```bash
yeedu workspace create-user-access --workspace_id=1 --user_id=1 --permission_id=2
```

- Console output

```bash
{
  "auth_workspace_user_id": "2",
  "workspace_id": "1",
  "auth_workspace_perm_id": 2,
  "user_id": "1",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-13T11:33:08.443Z",
  "from_date": "2024-06-13T11:33:08.443Z",
  "to_date": null
}
```

### create-group-access

```bash
yeedu workspace create-group-access -h
```

```bash
usage:  create-group-access [-h] --workspace_id WORKSPACE_ID
                            --group_id GROUP_ID --permission_id
                            PERMISSION_ID
                            [--json-output [{pretty,default}]]
                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to assign group access on a workspace.
  --group_id GROUP_ID   Provide group Id to assign group access on a workspace.
  --permission_id PERMISSION_ID
                        Provide Permission Id to assign group access on a workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-group-access example with optional arguments passed.

```bash
yeedu workspace create-group-access --workspace_id=1 --group_id=1 --permission_id=2
```

- Console output

```bash
{
  "auth_workspace_group_id": "1",
  "workspace_id": "1",
  "auth_workspace_perm_id": 2,
  "group_id": "1",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-13T11:34:14.175Z",
  "from_date": "2024-06-13T11:34:14.175Z",
  "to_date": null
}
```

### delete-user-access

```bash
yeedu workspace delete-user-access -h
```

```bash
usage:  delete-user-access [-h] --workspace_id WORKSPACE_ID --user_id USER_ID
                           --permission_id PERMISSION_ID
                           [--json-output [{pretty,default}]]
                           [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to delete user access on a workspace.
  --user_id USER_ID     Provide User Id to delete user access on a workspace.
  --permission_id PERMISSION_ID
                        Provide Permission Id to delete user access on a workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- delete-user-access example with the required argument passed.

```bash
yeedu workspace delete-user-access --workspace_id=1 --user_id=1 --permission_id=2
```

- Console output

```bash
{
  "message": "Deleted Permission successfully."
}
```

### delete-group-access

```bash
yeedu workspace delete-group-access -h
```

```bash
usage:  delete-group-access [-h] --workspace_id WORKSPACE_ID --group_id GROUP_ID
                            --permission_id PERMISSION_ID
                            [--json-output [{pretty,default}]]
                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to delete group access on a workspace.
  --group_id GROUP_ID   Provide group Id to delete group access on a workspace.
  --permission_id PERMISSION_ID
                        Provide Permission Id to delete group access on a workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- delete-group-access example with all the required arguments passed.

```bash
yeedu workspace delete-group-access --workspace_id=1 --group_id=1 --permission_id=2
```

- Console output

```bash
{
  "message": "Deleted Permission successfully."
}
```

### list-users

```bash
yeedu workspace list-users -h
```

```bash
usage:  list-users [-h] --workspace_id WORKSPACE_ID [--page_number PAGE_NUMBER]
                   [--limit LIMIT] [--json-output [{pretty,default}]]
                   [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to list all the users.
  --page_number PAGE_NUMBER
                        To list users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- list-users example with the required argument '--workspace_id' passed.

```bash
yeedu workspace list-users --workspace_id=1
```

- Console output

```bash
{
  "data": [
    {
      "user_id": 1,
      "username": "YSU0000",
      "display_name": "YSU0000",
      "email": "ysu0000@yeedu.com"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-users

```bash
yeedu workspace search-users -h
```

```bash
usage:  search-users [-h] --workspace_id WORKSPACE_ID --username USERNAME
                     [--page_number PAGE_NUMBER] [--limit LIMIT]
                     [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to search all the users.
  --username USERNAME   Provide username to search all the users.
  --page_number PAGE_NUMBER
                        To search users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- search example with the required argument passed.

```bash
yeedu workspace search-users --workspace_id=1 --username="YSU"
```

- Console output

```bash
{
  "data": [
    {
      "user_id": 1,
      "username": "YSU0000",
      "display_name": "YSU0000",
      "email": "ysu0000@yeedu.com"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### match-user

```bash
yeedu workspace match-user -h
```

```bash
usage:  match-user [-h] --workspace_id WORKSPACE_ID --username USERNAME
                   [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to match all the users.
  --username USERNAME   Provide username to match all the users.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- match example with the required argument passed.

```bash
yeedu workspace match-user --workspace_id=1 --username="YSU0000"
```

- Console output

```bash
{
  "user_id": 1,
  "username": "YSU0000",
  "display_name": "YSU0000",
  "email": "ysu0000@yeedu.com",
  "from_date": "2024-06-13T11:29:51.951785+00:00",
  "to_date": "infinity"
}
```

### list-groups

```bash
yeedu workspace list-groups -h
```

```bash
usage:  list-groups [-h] --workspace_id WORKSPACE_ID [--page_number PAGE_NUMBER]
                    [--limit LIMIT] [--json-output [{pretty,default}]]
                    [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to list all the groups.
  --page_number PAGE_NUMBER
                        To list groups for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of groups. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- list-groups example with the required argument '--workspace_id' passed.

```bash
yeedu workspace list-groups --workspace_id=1 --limit=1
```

- Console output

```bash
{
  "data": [
    {
      "group_id": 2,
      "group_name": "Yeedu",
      "group_type": "DynamicMembership",
      "from_date": "2023-12-28T14:01:50.367429+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 13,
    "total_pages": 13,
    "limit": 1,
    "next_page": 2
  }
}
```

### search-groups

```bash
yeedu workspace search-groups -h
```

```bash
usage:  search-groups [-h] --workspace_id WORKSPACE_ID --groupname GROUPNAME
                      [--page_number PAGE_NUMBER] [--limit LIMIT]
                      [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to search all the groups.
  --groupname GROUPNAME
                        Provide groupname to search all the groups.
  --page_number PAGE_NUMBER
                        To search groups for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of groups. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- search example with the required argument passed.

```bash
yeedu workspace search-groups --workspace_id=1 --groupname="Yeedu"
```

- Console output

```bash
{
  "data": [
    {
      "group_id": 7,
      "group_name": "Yeedu",
      "group_type": null,
      "from_date": "2023-12-28T14:01:50.367429+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 11,
      "group_name": "Yeedu Dev_Team",
      "group_type": null,
      "from_date": "2023-12-28T14:01:50.367429+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 25,
      "group_name": "Yeedu_Backend",
      "group_type": null,
      "from_date": "2024-01-02T09:19:25.770823+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 3,
    "total_pages": 1,
    "limit": 100
  }
}
```

### match-group

```bash
yeedu workspace match-group -h
```

```bash
usage:  match-group [-h] --workspace_id WORKSPACE_ID --groupname GROUPNAME
                    [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to match all the groups.
  --groupname GROUPNAME
                        Provide groupname to match all the groups.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- match example with the required argument passed.

```bash
yeedu workspace match-group --workspace_id=1 --groupname="Yeedu"
```

- Console output

```bash
[
  {
    "group_id": 8,
    "group_name": "Yeedu",
    "group_type": "Unified",
    "from_date": "2023-12-28T14:01:50.367429+00:00",
    "to_date": "infinity"
  },
  {
    "group_id": 7,
    "group_name": "Yeedu",
    "group_type": null,
    "from_date": "2023-12-28T14:01:50.367429+00:00",
    "to_date": "infinity"
  }
]
```

### get-user-access

```bash
yeedu workspace get-user-access -h
```

```bash
usage:  get-user-access [-h] --workspace_id WORKSPACE_ID --user_id USER_ID
                        [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to get the permission of a user.
  --user_id USER_ID     Provide User Id to get the permission of a user.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-user-access example with all the required arguments passed.

```bash
yeedu workspace get-user-access --workspace_id=1 --user_id=1
```

- Console output

```bash
{
  "user_id": "1",
  "username": "YSU0000",
  "workspace": {
    "workspace_id": "1",
    "name": "spark_jobs_test",
    "description": "Test Spark Curation Jobs"
  },
  "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
  "user_permission": {
    "auth_workspace_user_id": 3,
    "permission": {
      "auth_workspace_perm_id": 2,
      "name": "EDIT",
      "description": "To list, run and edit a spark job in a workspace"
    },
    "created_by": {
      "user_id": 1,
      "username": "YSU0000"
    },
    "modified_by": {
      "user_id": 1,
      "username": "YSU0000"
    },
    "last_update_date": "2024-06-13T11:59:27.373872+00:00",
    "from_date": "2024-06-13T11:59:27.373872+00:00",
    "to_date": "infinity"
  },
  "group_permission": [
    {
      "auth_workspace_group_id": 2,
      "permission": {
        "auth_workspace_perm_id": 2,
        "name": "EDIT",
        "description": "To list, run and edit a spark job in a workspace"
      },
      "group_id": 1,
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-06-13T12:01:10.81785+00:00",
      "from_date": "2024-06-13T12:01:10.81785+00:00",
      "to_date": "infinity"
    }
  ]
}
```

### get-group-access

```bash
yeedu workspace get-group-access -h
```

```bash
usage:  get-group-access [-h] --workspace_id WORKSPACE_ID --group_id GROUP_ID
                         [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to get the permission of a group.
  --group_id GROUP_ID   Provide Group Id to get the permission of a group.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-group-access example with all the required arguments passed.

```bash
yeedu workspace get-group-access --workspace_id=1 --group_id=1
```

- Console output

```bash
{
  "group_id": "1",
  "group_name": "yeedu-manager",
  "workspace": {
    "workspace_id": "1",
    "name": "spark_jobs_test",
    "description": "Test Spark Curation Jobs"
  },
  "tenant_id": "e67f00ad-68aa-46d0-b32e-f3f8dac5427d",
  "group_permission": {
    "auth_workspace_group_id": "1",
    "permission": {
      "auth_workspace_perm_id": 2,
      "name": "EDIT",
      "description": "To list, run and edit a spark job in a workspace"
    },
    "created_by": {
      "user_id": "1",
      "username": "YSU0000"
    },
    "modified_by": {
      "user_id": "1",
      "username": "YSU0000"
    },
    "last_update_date": "2024-01-08T14:00:26.953Z",
    "from_date": "2024-01-08T14:00:26.953Z",
    "to_date": null
  }
}
```

### list-users-access

```bash
yeedu workspace list-users-access -h
```

```bash
usage:  list-users-access [-h] --workspace_id WORKSPACE_ID
                          [--permission_id PERMISSION_ID] [--page_number PAGE_NUMBER]
                          [--limit LIMIT] [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Specifies the ID of the workspace to retrieve users from.
  --permission_id PERMISSION_ID
                        Specifies the ID of the permission to retrieve users.
  --page_number PAGE_NUMBER
                        To list users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- list-users-access example with the required argument '--workspace_id' passed.

```bash
yeedu workspace list-users-access --workspace_id=1
```

- Console output

```bash
{
  "data": {
    "workspace_id": 1,
    "workspace_name": "yeedu_workspace",
    "description": null,
    "users": [
      {
        "user_id": 50,
        "username": "yeedu@yeedu.io",
        "email": "yeedu@yeedu.io",
        "display_name": "Yeedu",
        "permission": {
          "permission_id": 3,
          "name": "MANAGE",
          "description": "To list jobs, run jobs, edit Spark jobs, and manage workspace access by adding or removing permissions"
        }
      },
      ...
      {
        "user_id": 1,
        "username": "yeedu.test@yeedu.io",
        "email": "yeedu-test@yeedu.io",
        "display_name": "Yeedu Test",
        "permission": {
          "permission_id": 2,
          "name": "EDIT",
          "description": "To list, run and edit a spark job in a workspace"
        }
      }
    ]
  },
  "result_set": {
    "current_page": 1,
    "total_objects": 50,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-users-access

```bash
yeedu workspace search-users-access -h
```

```bash
usage:  search-users-access [-h] --workspace_id WORKSPACE_ID --username USERNAME
                            [--permission_id PERMISSION_ID] [--page_number PAGE_NUMBER]
                            [--limit LIMIT] [--json-output [{pretty,default}]]
                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Specifies the ID of the workspace to search users from.
  --username USERNAME   Specifies username to retrieve users.
  --permission_id PERMISSION_ID
                        Specifies the ID of the permission to retrieve users.
  --page_number PAGE_NUMBER
                        To list users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- search-users-access example with the required argument '--workspace_id' and '--username' passed.

```bash
yeedu workspace search-users-access --workspace_id=1 --username='yeedu'
```

- Console output

```bash
{
  "data": {
    "workspace_id": 1,
    "workspace_name": "yeedu_workspace",
    "description": null,
    "users": [
      {
        "user_id": 1,
        "username": "yeedu@yeedu.io",
        "email": "yeedu@yeedu.io",
        "display_name": "Yeedu",
        "permission": {
          "permission_id": 3,
          "name": "MANAGE",
          "description": "To list jobs, run jobs, edit Spark jobs, and manage workspace access by adding or removing permissions"
        }
      }
    ]
  },
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### list-groups-access

```bash
yeedu workspace list-groups-access -h
```

```bash
usage:  list-groups-access [-h] --workspace_id WORKSPACE_ID
                           [--permission_id PERMISSION_ID] [--page_number PAGE_NUMBER]
                           [--limit LIMIT] [--json-output [{pretty,default}]]
                           [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Specifies the ID of the workspace to list groups from.
  --permission_id PERMISSION_ID
                        Specifies the ID of the permission to retrieve groups.
  --page_number PAGE_NUMBER
                        To list groups for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of groups. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- list-groups-access example with the required argument '--workspace_id' passed.

```bash
yeedu workspace list-groups-access --workspace_id=1
```

- Console output

```bash
{
  "data": {
    "workspace_id": 1,
    "workspace_name": "yeed_workspace",
    "description": null,
    "groups": [
      {
        "group_id": 1,
        "group_name": "Yeedu Dev",
        "group_mail": yeedu-dev@yeedu.io,
        "group_object_id": "bbdfd7a7-d0d3-4f32-8d7c-c33a1292222",
        "group_type": null,
        "permission": {
          "permission_id": 2,
          "name": "EDIT",
          "description": "To list, run and edit a spark job in a workspace"
        }
      }
    ]
  },
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-groups-access

```bash
yeedu workspace search-groups-access -h
```

```bash
usage:  search-groups-access [-h] --workspace_id WORKSPACE_ID --groupname GROUPNAME
                             [--permission_id PERMISSION_ID] [--page_number PAGE_NUMBER]
                             [--limit LIMIT] [--json-output [{pretty,default}]]
                             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Specifies the ID of the workspace to search groups from.
  --groupname GROUPNAME
                        Specifies groupname to retrieve groups.
  --permission_id PERMISSION_ID
                        Specifies the ID of the permission to retrieve groups.
  --page_number PAGE_NUMBER
                        To list groups for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of groups. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- list-groups-access example with the required argument '--workspace_id' passed.

```bash
yeedu workspace search-groups-access --workspace_id=1 --groupname="Yeedu"
```

- Console output

```bash
{
  "data": {
    "workspace_id": 1,
    "workspace_name": "yeed_workspace",
    "description": null,
    "groups": [
      {
        "group_id": 1,
        "group_name": "Yeedu Dev",
        "group_mail": yeedu-dev@yeedu.io,
        "group_object_id": "bbdfd7a7-d0d3-4f32-8d7c-c33a1292222",
        "group_type": null,
        "permission": {
          "permission_id": 2,
          "name": "EDIT",
          "description": "To list, run and edit a spark job in a workspace"
        }
      }
    ]
  },
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

# Job

## Spark Job

| Command Name        | Utility                                            |
| ------------------- | ---------------------------------------------------|
| [create](#create)   | To create the Spark Job.                           |
| [list](#list)       | To list all the available Job.                     |
| [search](#search)   | To search job by job name in a workspace.          |
| [get](#get)         | To get the information about a specific Spark Job. |
| [edit](#edit)       | To edit the Spark Job.                             |
| [enable](#enable)   | To enable a specific Spark Job.                    |
| [disable](#disable) | To disable a specific Spark Job.                   |
| [export](#export)   | Export a specific Spark Job.                       |

### create

```bash
yeedu job create -h
```

```bash
usage:  create [-h] [--cluster_id CLUSTER_ID] [--cluster_name CLUSTER_NAME] --workspace_id WORKSPACE_ID --name JOB_NAME [--files [FILES]] [--properties-file [PROPERTIES_FILE]] [--conf CONF [CONF ...]]
               [--packages [PACKAGES]] [--repositories [REPOSITORIES]] [--jars [JARS]] [--archives [ARCHIVES]] [--driver-memory [DRIVER_MEMORY]] [--driver-java-options [DRIVER_JAVA_OPTIONS]]
               [--driver-library-path [DRIVER_LIBRARY_PATH]] [--driver-class-path [DRIVER_CLASS_PATH]] [--executor-memory [EXECUTOR_MEMORY]] [--driver-cores [DRIVER_CORES]]
               [--total-executor-cores [TOTAL_EXECUTOR_CORES]] [--executor-cores [EXECUTOR_CORES]] [--num-executors [NUM_EXECUTORS]] [--should_append_params [{true,false}]] [--principal [PRINCIPAL]] [--keytab [KEYTAB]]
               [--queue [QUEUE]] [--job-class-name [JOB_CLASS_NAME]] [--job-command [JOB_COMMAND]] [--job-arguments [JOB_ARGUMENTS]] [--job-raw-scala-code JOB_RAW_SCALA_CODE] --job-type
               {RAW_SCALA,Jar,Python3,SQL,THRIFT_SQL,YEEDU_FUNCTIONS} [--job-timeout-min JOB_TIMEOUT_MIN] [--max_concurrency MAX_CONCURRENCY] [--yeedu-functions-project-path [YEEDU_FUNCTIONS_PROJECT_PATH]]
               [--yeedu-functions-script-path [YEEDU_FUNCTIONS_SCRIPT_PATH]] [--yeedu-functions-function-name YEEDU_FUNCTIONS_FUNCTION_NAME] [--yeedu-functions-requirements [YEEDU_FUNCTIONS_REQUIREMENTS]]
               [--yeedu-functions-max-request-concurrency [YEEDU_FUNCTIONS_MAX_REQUEST_CONCURRENCY]] [--yeedu-functions-request-timeout-sec [YEEDU_FUNCTIONS_REQUEST_TIMEOUT_SEC]]
               [--yeedu-functions-idle-timeout-sec [YEEDU_FUNCTIONS_IDLE_TIMEOUT_SEC]] [--yeedu-functions-example-request-body [YEEDU_FUNCTIONS_EXAMPLE_REQUEST_BODY]] [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --cluster_id CLUSTER_ID
                        Provide cluster_id to create a Spark Job.
  --cluster_name CLUSTER_NAME
                        Provide cluster_name to create a Spark Job.
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to create a Spark Job.
  --name JOB_NAME       Provide name to create a Spark Job.
  --files [FILES]       Provide files to create a Spark Job.
  --properties-file [PROPERTIES_FILE]
                        Provide properties-file to create a Spark Job.
  --conf CONF [CONF ...]
                        Provide conf to create a Spark Job.
  --packages [PACKAGES]
                        Provide packages to create a Spark Job.
  --repositories [REPOSITORIES]
                        Provide repositories to create a Spark Job.
  --jars [JARS]         Provide jars to create a Spark Job.
  --archives [ARCHIVES]
                        Provide archives to create a Spark Job.
  --driver-memory [DRIVER_MEMORY]
                        Provide driver-memory to create a Spark Job.
  --driver-java-options [DRIVER_JAVA_OPTIONS]
                        Provide driver-java-options to create a Spark Job.
  --driver-library-path [DRIVER_LIBRARY_PATH]
                        Provide driver-library-path to create a Spark Job.
  --driver-class-path [DRIVER_CLASS_PATH]
                        Provide driver-class-path to create a Spark Job.
  --executor-memory [EXECUTOR_MEMORY]
                        Provide executor-memory to create a Spark Job.
  --driver-cores [DRIVER_CORES]
                        Provide driver-cores to create a Spark Job.
  --total-executor-cores [TOTAL_EXECUTOR_CORES]
                        Provide total-executor-cores to create a Spark Job.
  --executor-cores [EXECUTOR_CORES]
                        Provide executor-cores to create a Spark Job.
  --num-executors [NUM_EXECUTORS]
                        Provide num-executors to create a Spark Job.
  --should_append_params [{true,false}]
                        Determines whether the job-level Spark configuration should append to or override the cluster-level Spark configuration.
  --principal [PRINCIPAL]
                        Provide principal to create a Spark Job.
  --keytab [KEYTAB]     Provide keytab to create a Spark Job.
  --queue [QUEUE]       Provide queue to create a Spark Job.
  --job-class-name [JOB_CLASS_NAME]
                        Provide job-class-name to create a Spark Job.
  --job-command [JOB_COMMAND]
                        Provide job-command to create a Spark Job.
  --job-arguments [JOB_ARGUMENTS]
                        Provide job-arguments to create a Spark Job.
  --job-raw-scala-code JOB_RAW_SCALA_CODE
                        Provide job-raw-scala-code file path to create a Spark Job.
  --job-type {RAW_SCALA,Jar,Python3,SQL,THRIFT_SQL,YEEDU_FUNCTIONS}
                        Provide job-type to create a Spark Job.
  --job-timeout-min JOB_TIMEOUT_MIN
                        Provide job-timeout-min to create a Spark Job.
  --max_concurrency MAX_CONCURRENCY
                        Provide max_concurrency number to limit the number of jobs submitted.
  --yeedu-functions-project-path [YEEDU_FUNCTIONS_PROJECT_PATH]
                        Provide yeedu-functions-project-path to create a Spark Job.
  --yeedu-functions-script-path [YEEDU_FUNCTIONS_SCRIPT_PATH]
                        Provide yeedu-functions-script-path to create a Spark Job.
  --yeedu-functions-function-name YEEDU_FUNCTIONS_FUNCTION_NAME
                        Provide yeedu-functions-function-name to create a Spark Job.
  --yeedu-functions-requirements [YEEDU_FUNCTIONS_REQUIREMENTS]
                        Provide yeedu-functions-requirements to create a Spark Job.
  --yeedu-functions-max-request-concurrency [YEEDU_FUNCTIONS_MAX_REQUEST_CONCURRENCY]
                        Provide yeedu-functions-max-request-concurrency to create a Spark Job.
  --yeedu-functions-request-timeout-sec [YEEDU_FUNCTIONS_REQUEST_TIMEOUT_SEC]
                        Provide yeedu-functions-request-timeout-sec to create a Spark Job.
  --yeedu-functions-idle-timeout-sec [YEEDU_FUNCTIONS_IDLE_TIMEOUT_SEC]
                        Provide yeedu-functions-idle-timeout-sec to create a Spark Job.
  --yeedu-functions-example-request-body [YEEDU_FUNCTIONS_EXAMPLE_REQUEST_BODY]
                        Provide yeedu-functions-example-request-body to create a Spark Job.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create example with all the required and optional arguments passed.

```bash
 yeedu job create --cluster_id=2 --workspace_id=1 --name="spark_examples" --job-class-name="org.apache.spark.examples.SparkPi" --job-command="file:///yeedu/object-storage-manager/spark-examples_2.12-3.2.2.jar" --job-arguments=500 --job-type=Jar
```

- Console output

```bash
{
  "job_id": "534876",
  "job_name": "spark_examples",
  "cluster_id": "2",
  "workspace_id": "1",
  "spark_job_type_lang_id": 1,
  "max_concurrency": "0",
  "job_class_name": "org.apache.spark.examples.SparkPi",
  "job_command": "file:///yeedu/object-storage-manager/spark-examples_2.12-3.2.2.jar",
  "job_arguments": "500",
  "job_rawScalaCode": null,
  "job_timeout_min": null,
  "files": null,
  "properties_file": null,
  "conf": null,
  "packages": null,
  "repositories": null,
  "jars": null,
  "archives": null,
  "driver_memory": null,
  "driver_java_options": null,
  "driver_library_path": null,
  "driver_class_path": null,
  "executor_memory": null,
  "driver_cores": null,
  "total_executor_cores": null,
  "executor_cores": null,
  "num_executors": null,
  "should_append_params": false,
  "principal": null,
  "keytab": null,
  "queue": null,
  "yeedu_functions_project_path": null,
  "yeedu_functions_script_path": null,
  "yeedu_functions_function_name": null,
  "yeedu_functions_requirements": null,
  "yeedu_functions_max_request_concurrency": null,
  "yeedu_functions_request_timeout_sec": null,
  "yeedu_functions_idle_timeout_sec": null,
  "yeedu_functions_example_request_body": null,
  "created_by_user_id": "8",
  "modified_by_user_id": "8",
  "last_update_date": "2025-06-26T08:03:42.948Z",
  "from_date": "2025-06-26T08:03:42.948Z",
  "to_date": null
}

```

### list

```bash
yeedu job list -h
```

```bash
usage:  list [-h] --workspace_id WORKSPACE_ID [--enable [{true,false}]] [--cluster_ids [CLUSTER_IDS]] [--job_type [JOB_TYPE]] [--job_type_langs [JOB_TYPE_LANGS]] [--last_run_status [LAST_RUN_STATUS]]
             [--created_by_ids [CREATED_BY_IDS]] [--modified_by_ids [MODIFIED_BY_IDS]] [--page_number PAGE_NUMBER] [--limit LIMIT] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        To list Jobs of a specific workspace.
  --enable [{true,false}]
                        Provide enable as true or false to list Jobs of a specific workspace.
  --cluster_ids [CLUSTER_IDS]
                        An optional set of cluster instance IDs to filter on.
  --job_type [JOB_TYPE]
                        An optional set of job types filter for Spark Job Choices are: SPARK_JOB, SPARK_SQL, THRIFT_SQL, YEEDU_FUNCTIONS
  --job_type_langs [JOB_TYPE_LANGS]
                        An optional set of language filter for Spark Job Choices are: RAW_SCALA, Jar, Python3, SQL
  --last_run_status [LAST_RUN_STATUS]
                        An optional set of last run statuses to filter Spark Job Choices are: submitted, running, done, error, terminated, stopping, stopped
  --created_by_ids [CREATED_BY_IDS]
                        An optional set of created by user IDs to filter on.
  --modified_by_ids [MODIFIED_BY_IDS]
                        An optional set of modified by user IDs to filter on.
  --page_number PAGE_NUMBER
                        To list Jobs for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of Job (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list example with required and optional arguments passed.

```bash
yeedu job list --workspace_id=1 --limit=1
```

- Console output

```bash
{
  "data": [
    {
      "job_id": 534876,
      "job_name": "spark_examples",
      "spark_job_type": {
        "job_type": "SPARK_JOB",
        "language": "Jar"
      },
      "cluster_info": {
        "cluster_id": 2,
        "name": "gcp_yeedu_3.4.3_50k",
        "cluster_status": "DESTROYED",
        "cluster_type": "YEEDU",
        "instance_size": 0,
        "min_instances": 1,
        "max_instances": 3,
        "is_turbo_enabled": false,
        "is_cuda_enabled": false,
        "cloud_env": {
          "cloud_env_id": 1,
          "name": "gcp_env",
          "cloud_provider": {
            "cloud_provider_id": 0,
            "name": "GCP"
          }
        },
        "cluster_conf": {
          "cluster_conf_id": 12,
          "cluster_conf_name": "n1-standard-8",
          "machine_type_category": "general_purpose",
          "machine_type": {
            "machine_type_id": 12,
            "name": "n1-standard-8",
            "vCPUs": 8,
            "memory": "30 GiB",
            "has_cuda": false,
            "gpu_model": null,
            "gpus": 0,
            "gpu_memory": null,
            "cpu_model": [
              "Intel Xeon Scalable (Skylake) 1st Generation",
              "Intel Xeon E5 v4 (Broadwell E5)",
              "Intel Xeon E5 v3 (Haswell)",
              "Intel Xeon E5 v2 (Ivy Bridge)",
              "Intel Xeon E5 (Sandy Bridge)"
            ],
            "cpu_min_frequency_GHz": [
              "2.0",
              "2.2",
              "2.3",
              "2.5",
              "2.6"
            ],
            "cpu_max_frequency_GHz": [
              "3.5",
              "3.7",
              "3.8",
              "3.5",
              "3.6"
            ],
            "has_local_disk": false,
            "local_disk_size_GB": null,
            "local_num_of_disks": null,
            "local_disk_throughput_MB": null,
            "has_spot_instance_support": true,
            "machine_price_ycu": 5
          },
          "machine_volume_conf": {
            "volume_conf_id": 2,
            "name": "volume_gcp_2",
            "size": 375,
            "machine_volume_num": 2,
            "machine_volume_strip_num": 2
          }
        },
        "spark_infra_version": {
          "spark_infra_version_id": 3,
          "spark_docker_image_name": "v3.4.3-5",
          "spark_version": "3.4.3",
          "hive_version": "2.3.9",
          "hadoop_version": "3.2.4",
          "scala_version": "2.12.15",
          "python_version": "3.9.5",
          "notebook_support": true,
          "has_cuda_support": true,
          "thrift_support": true,
          "yeedu_functions_support": true,
          "has_turbo_support": true,
          "turbo_version": "v1.0.6",
          "has_unity_support": false,
          "unity_version": null,
          "has_hive_support": true,
          "cuda_rapids_version": "23.04.1"
        },
        "engine_cluster_spark_config": {
          "max_parallel_spark_job_execution_per_instance": 5,
          "num_of_workers": null
        }
      },
      "last_job_run": {
        "job_id": null,
        "run_status": null
      },
      "created_by": {
        "user_id": 8,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 8,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2025-06-26T08:03:42.948981+00:00",
      "from_date": "2025-06-26T08:03:42.948981+00:00",
      "to_date": "infinity"
    }
  ]
}
```

### search

```bash
yeedu job search -h
```

```bash
usage:  search [-h] --workspace_id WORKSPACE_ID --job_name JOB_NAME [--enable [{true,false}]] [--cluster_ids [CLUSTER_IDS]] [--job_type [JOB_TYPE]] [--job_type_langs [JOB_TYPE_LANGS]]
               [--last_run_status [LAST_RUN_STATUS]] [--created_by_ids [CREATED_BY_IDS]] [--modified_by_ids [MODIFIED_BY_IDS]] [--page_number PAGE_NUMBER] [--limit LIMIT] [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to search jobs in it.
  --job_name JOB_NAME   Provide job_name to search Job
  --enable [{true,false}]
                        Provide enable as true or false to search Job
  --cluster_ids [CLUSTER_IDS]
                        An optional set of cluster instance IDs to filter on.
  --job_type [JOB_TYPE]
                        An optional set of job types filter for Spark Job Choices are: SPARK_JOB, SPARK_SQL, THRIFT_SQL, YEEDU_FUNCTIONS
  --job_type_langs [JOB_TYPE_LANGS]
                        An optional set of language filter for Spark Job Choices are: RAW_SCALA, Jar, Python3, SQL
  --last_run_status [LAST_RUN_STATUS]
                        An optional set of last run statuses to filter Spark Job Choices are: submitted, running, done, error, terminated, stopping, stopped
  --created_by_ids [CREATED_BY_IDS]
                        An optional set of created by user IDs to filter on.
  --modified_by_ids [MODIFIED_BY_IDS]
                        An optional set of modified by user IDs to filter on.
  --page_number PAGE_NUMBER
                        To search jobs for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of Job (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search example with required and optional arguments passed.

```bash
yeedu job search --workspace_id=1 --job_name="spark_" --enable=true --limit=2
```

- Console output

```bash
{
  "data": [
    {
      "job_id": 534876,
      "job_name": "spark_examples",
      "spark_job_type": {
        "job_type": "SPARK_JOB",
        "language": "Jar"
      },
      "cluster_info": {
        "cluster_id": 2,
        "name": "gcp_yeedu_3.4.3_50k",
        "cluster_status": "DESTROYED",
        "cluster_type": "YEEDU",
        "instance_size": 0,
        "min_instances": 1,
        "max_instances": 3,
        "is_turbo_enabled": false,
        "is_cuda_enabled": false,
        "cloud_env": {
          "cloud_env_id": 1,
          "name": "gcp_env",
          "cloud_provider": {
            "cloud_provider_id": 0,
            "name": "GCP"
          }
        },
        "cluster_conf": {
          "cluster_conf_id": 12,
          "cluster_conf_name": "n1-standard-8",
          "machine_type_category": "general_purpose",
          "machine_type": {
            "machine_type_id": 12,
            "name": "n1-standard-8",
            "vCPUs": 8,
            "memory": "30 GiB",
            "has_cuda": false,
            "gpu_model": null,
            "gpus": 0,
            "gpu_memory": null,
            "cpu_model": [
              "Intel Xeon Scalable (Skylake) 1st Generation",
              "Intel Xeon E5 v4 (Broadwell E5)",
              "Intel Xeon E5 v3 (Haswell)",
              "Intel Xeon E5 v2 (Ivy Bridge)",
              "Intel Xeon E5 (Sandy Bridge)"
            ],
            "cpu_min_frequency_GHz": [
              "2.0",
              "2.2",
              "2.3",
              "2.5",
              "2.6"
            ],
            "cpu_max_frequency_GHz": [
              "3.5",
              "3.7",
              "3.8",
              "3.5",
              "3.6"
            ],
            "has_local_disk": false,
            "local_disk_size_GB": null,
            "local_num_of_disks": null,
            "local_disk_throughput_MB": null,
            "has_spot_instance_support": true,
            "machine_price_ycu": 5
          },
          "machine_volume_conf": {
            "volume_conf_id": 2,
            "name": "volume_gcp_2",
            "size": 375,
            "machine_volume_num": 2,
            "machine_volume_strip_num": 2
          }
        },
        "spark_infra_version": {
          "spark_infra_version_id": 3,
          "spark_docker_image_name": "v3.4.3-5",
          "spark_version": "3.4.3",
          "hive_version": "2.3.9",
          "hadoop_version": "3.2.4",
          "scala_version": "2.12.15",
          "python_version": "3.9.5",
          "notebook_support": true,
          "has_cuda_support": true,
          "thrift_support": true,
          "yeedu_functions_support": true,
          "has_turbo_support": true,
          "turbo_version": "v1.0.6",
          "has_unity_support": false,
          "unity_version": null,
          "has_hive_support": true,
          "cuda_rapids_version": "23.04.1"
        },
        "engine_cluster_spark_config": {
          "max_parallel_spark_job_execution_per_instance": 5,
          "num_of_workers": null
        }
      },
      "last_job_run": {
        "job_id": null,
        "run_status": null
      },
      "created_by": {
        "user_id": 8,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 8,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2025-06-26T08:03:42.948981+00:00",
      "from_date": "2025-06-26T08:03:42.948981+00:00",
      "to_date": "infinity"
    }
  ]
}
```

### get

```bash
yeedu job get -h
```

```bash
usage:  get [-h] --workspace_id WORKSPACE_ID [--job_id JOB_ID] [--job_name JOB_NAME] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to get information about a specific Spark Job.
  --job_id JOB_ID       Provide Job Id to get information about a specific Spark Job.
  --job_name JOB_NAME   Provide Job name to get information about a specific Spark Job.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get example with the optional and required argument passed.

```bash
  yeedu job get --workspace_id=1 --job_id=1
```

- Console output

```bash
{
  "job_id": 1,
  "job_name": "job_load_test_813cdc68-2ae0-4c8f-8ab7-bcdfe926ee44",
  "cluster_info": {
    "cluster_id": 2,
    "name": "gcp_yeedu_3.4.3_50k",
    "cluster_status": "DESTROYED",
    "cluster_type": "YEEDU",
    "instance_size": 0,
    "min_instances": 1,
    "max_instances": 3,
    "is_turbo_enabled": false,
    "is_cuda_enabled": false,
    "cluster_conf": {
      "cluster_conf_id": 12,
      "cluster_conf_name": "n1-standard-8",
      "machine_type_category": "general_purpose",
      "machine_type": {
        "machine_type_id": 12,
        "name": "n1-standard-8",
        "vCPUs": 8,
        "memory": "30 GiB",
        "has_cuda": false,
        "gpu_model": null,
        "gpus": 0,
        "gpu_memory": null,
        "cpu_model": [
          "Intel Xeon Scalable (Skylake) 1st Generation",
          "Intel Xeon E5 v4 (Broadwell E5)",
          "Intel Xeon E5 v3 (Haswell)",
          "Intel Xeon E5 v2 (Ivy Bridge)",
          "Intel Xeon E5 (Sandy Bridge)"
        ],
        "cpu_min_frequency_GHz": [
          "2.0",
          "2.2",
          "2.3",
          "2.5",
          "2.6"
        ],
        "cpu_max_frequency_GHz": [
          "3.5",
          "3.7",
          "3.8",
          "3.5",
          "3.6"
        ],
        "has_local_disk": false,
        "local_disk_size_GB": null,
        "local_num_of_disks": null,
        "local_disk_throughput_MB": null,
        "has_spot_instance_support": true,
        "machine_price_ycu": 5
      },
      "machine_volume_conf": {
        "volume_conf_id": 2,
        "name": "volume_gcp_2",
        "size": 375,
        "machine_volume_num": 2,
        "machine_volume_strip_num": 2
      }
    },
    "cloud_env": {
      "cloud_env_id": 1,
      "name": "gcp_env",
      "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP"
      }
    },
    "spark_infra_version": {
      "spark_infra_version_id": 3,
      "spark_docker_image_name": "v3.4.3-5",
      "spark_version": "3.4.3",
      "hive_version": "2.3.9",
      "hadoop_version": "3.2.4",
      "scala_version": "2.12.15",
      "python_version": "3.9.5",
      "notebook_support": true,
      "has_cuda_support": true,
      "thrift_support": true,
      "yeedu_functions_support": true,
      "has_turbo_support": true,
      "turbo_version": "v1.0.6",
      "has_unity_support": false,
      "unity_version": null,
      "has_hive_support": true,
      "cuda_rapids_version": "23.04.1"
    },
    "engine_cluster_spark_config": {
      "max_parallel_spark_job_execution_per_instance": 5,
      "num_of_workers": null
    }
  },
  "spark_job_type": {
    "job_type": "SPARK_JOB",
    "language": "Jar"
  },
  "max_concurrency": 1,
  "job_class_name": "org.apache.spark.examples.SparkPi",
  "job_command": "/opt/spark/examples/jars/spark-examples_2.12-3.4.3.jar",
  "job_arguments": "1",
  "job_rawScalaCode": null,
  "job_timeout_min": null,
  "files": null,
  "properties_file": null,
  "conf": null,
  "packages": null,
  "repositories": null,
  "jars": null,
  "archives": null,
  "driver_memory": null,
  "driver_java_options": null,
  "driver_library_path": null,
  "driver_class_path": null,
  "executor_memory": null,
  "driver_cores": null,
  "total_executor_cores": null,
  "executor_cores": null,
  "num_executors": null,
  "should_append_params": false,
  "principal": null,
  "keytab": null,
  "queue": null,
  "yeedu_functions_script_path": null,
  "yeedu_functions_function_name": null,
  "yeedu_functions_requirements": null,
  "yeedu_functions_max_request_concurrency": null,
  "yeedu_functions_idle_timeout_sec": null,
  "yeedu_functions_request_timeout_sec": null,
  "yeedu_functions_project_path": null,
  "yeedu_functions_example_request_body": null,
  "tenant_id": "9fcc8aef-3b7f-4495-8ffb-9c35399715a0",
  "created_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "last_update_date": "2025-05-16T08:39:26.929624+00:00",
  "from_date": "2025-05-16T08:39:26.929624+00:00",
  "to_date": "infinity"
}

```

### edit

```bash
yeedu job edit -h
```

```bash
usage:  edit [-h] --workspace_id WORKSPACE_ID [--job_id JOB_ID] [--job_name JOB_NAME] [--cluster_id CLUSTER_ID] [--cluster_name CLUSTER_NAME] [--files [FILES]] [--properties-file [PROPERTIES_FILE]]
             [--conf CONF [CONF ...]] [--packages [PACKAGES]] [--repositories [REPOSITORIES]] [--jars [JARS]] [--archives [ARCHIVES]] [--driver-memory [DRIVER_MEMORY]]
             [--driver-java-options [DRIVER_JAVA_OPTIONS]] [--driver-library-path [DRIVER_LIBRARY_PATH]] [--driver-class-path [DRIVER_CLASS_PATH]] [--executor-memory [EXECUTOR_MEMORY]]
             [--driver-cores [DRIVER_CORES]] [--total-executor-cores [TOTAL_EXECUTOR_CORES]] [--executor-cores [EXECUTOR_CORES]] [--num-executors [NUM_EXECUTORS]] [--should_append_params [{true,false}]]
             [--principal [PRINCIPAL]] [--keytab [KEYTAB]] [--queue [QUEUE]] [--job-class-name [JOB_CLASS_NAME]] [--name [NAME]] [--job-command [JOB_COMMAND]] [--job-arguments [JOB_ARGUMENTS]]
             [--job-raw-scala-code JOB_RAW_SCALA_CODE] [--job-timeout-min JOB_TIMEOUT_MIN] [--max_concurrency MAX_CONCURRENCY] [--yeedu-functions-project-path [YEEDU_FUNCTIONS_PROJECT_PATH]]
             [--yeedu-functions-script-path [YEEDU_FUNCTIONS_SCRIPT_PATH]] [--yeedu-functions-function-name YEEDU_FUNCTIONS_FUNCTION_NAME] [--yeedu-functions-requirements [YEEDU_FUNCTIONS_REQUIREMENTS]]
             [--yeedu-functions-max-request-concurrency [YEEDU_FUNCTIONS_MAX_REQUEST_CONCURRENCY]] [--yeedu-functions-request-timeout-sec [YEEDU_FUNCTIONS_REQUEST_TIMEOUT_SEC]]
             [--yeedu-functions-idle-timeout-sec [YEEDU_FUNCTIONS_IDLE_TIMEOUT_SEC]] [--yeedu-functions-example-request-body [YEEDU_FUNCTIONS_EXAMPLE_REQUEST_BODY]] [--json-output [{pretty,default}]]
             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to edit a Spark Job.
  --job_id JOB_ID       Provide Job Id to edit a Spark Job.
  --job_name JOB_NAME   Provide Job Name to edit a Spark Job.
  --cluster_id CLUSTER_ID
                        Provide cluster_id to edit a Spark Job.
  --cluster_name CLUSTER_NAME
                        Provide cluster_name to edit a Spark Job.
  --files [FILES]       Provide files to edit a Spark Job.
  --properties-file [PROPERTIES_FILE]
                        Provide properties-file to edit a Spark Job.
  --conf CONF [CONF ...]
                        Provide conf to edit a Spark Job.
  --packages [PACKAGES]
                        Provide packages to edit a Spark Job.
  --repositories [REPOSITORIES]
                        Provide repositories to edit a Spark Job.
  --jars [JARS]         Provide jars to edit a Spark Job.
  --archives [ARCHIVES]
                        Provide archives to edit a Spark Job.
  --driver-memory [DRIVER_MEMORY]
                        Provide driver-memory to edit a Spark Job.
  --driver-java-options [DRIVER_JAVA_OPTIONS]
                        Provide driver-java-options to edit a Spark Job.
  --driver-library-path [DRIVER_LIBRARY_PATH]
                        Provide driver-library-path to edit a Spark Job.
  --driver-class-path [DRIVER_CLASS_PATH]
                        Provide driver-class-path to edit a Spark Job.
  --executor-memory [EXECUTOR_MEMORY]
                        Provide executor-memory to edit a Spark Job.
  --driver-cores [DRIVER_CORES]
                        Provide driver-cores to edit a Spark Job.
  --total-executor-cores [TOTAL_EXECUTOR_CORES]
                        Provide total-executor-cores to edit a Spark Job.
  --executor-cores [EXECUTOR_CORES]
                        Provide executor-cores to edit a Spark Job.
  --num-executors [NUM_EXECUTORS]
                        Provide num-executors to edit a Spark Job.
  --should_append_params [{true,false}]
                        Determines whether the job-level Spark configuration should append to or override the cluster-level Spark configuration.
  --principal [PRINCIPAL]
                        Provide principal to edit a Spark Job.
  --keytab [KEYTAB]     Provide keytab to edit a Spark Job.
  --queue [QUEUE]       Provide queue to edit a Spark Job.
  --job-class-name [JOB_CLASS_NAME]
                        Provide job-class-name to edit a Spark Job.
  --name [NAME]         Provide name to edit a Spark Job.
  --job-command [JOB_COMMAND]
                        Provide job-command to edit a Spark Job.
  --job-arguments [JOB_ARGUMENTS]
                        Provide job-arguments to edit a Spark Job.
  --job-raw-scala-code JOB_RAW_SCALA_CODE
                        Provide job-raw-scala-code file path to edit a Spark Job.
  --job-timeout-min JOB_TIMEOUT_MIN
                        Provide job-timeout-min to edit a Spark Job.
  --max_concurrency MAX_CONCURRENCY
                        Provide max_concurrency number to limit the number of jobs submitted.
  --yeedu-functions-project-path [YEEDU_FUNCTIONS_PROJECT_PATH]
                        Provide yeedu-functions-project-path to edit a Spark Job.
  --yeedu-functions-script-path [YEEDU_FUNCTIONS_SCRIPT_PATH]
                        Provide yeedu-functions-script-path to edit a Spark Job.
  --yeedu-functions-function-name YEEDU_FUNCTIONS_FUNCTION_NAME
                        Provide yeedu-functions-function-name to edit a Spark Job.
  --yeedu-functions-requirements [YEEDU_FUNCTIONS_REQUIREMENTS]
                        Provide yeedu-functions-requirements to edit a Spark Job.
  --yeedu-functions-max-request-concurrency [YEEDU_FUNCTIONS_MAX_REQUEST_CONCURRENCY]
                        Provide yeedu-functions-max-request-concurrency to edit a Spark Job.
  --yeedu-functions-request-timeout-sec [YEEDU_FUNCTIONS_REQUEST_TIMEOUT_SEC]
                        Provide yeedu-functions-request-timeout-sec to edit a Spark Job.
  --yeedu-functions-idle-timeout-sec [YEEDU_FUNCTIONS_IDLE_TIMEOUT_SEC]
                        Provide yeedu-functions-idle-timeout-sec to edit a Spark Job.
  --yeedu-functions-example-request-body [YEEDU_FUNCTIONS_EXAMPLE_REQUEST_BODY]
                        Provide yeedu-functions-example-request-body to edit a Spark Job.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- edit example with the required arguments and other optional arguments passed which is to be updated.

```bash
yeedu job edit --workspace_id=1 --job_name="spark_examples" --job-arguments=1000
```

- Console output

```bash
{
  "job_id": "534876",
  "job_name": "spark_examples",
  "cluster_id": "2",
  "workspace_id": "1",
  "spark_job_type_lang_id": 1,
  "max_concurrency": "0",
  "job_class_name": "org.apache.spark.examples.SparkPi",
  "job_command": "file:///yeedu/object-storage-manager/spark-examples_2.12-3.2.2.jar",
  "job_arguments": "1000",
  "job_rawScalaCode": null,
  "job_timeout_min": null,
  "files": null,
  "properties_file": null,
  "conf": null,
  "packages": null,
  "repositories": null,
  "jars": null,
  "archives": null,
  "driver_memory": null,
  "driver_java_options": null,
  "driver_library_path": null,
  "driver_class_path": null,
  "executor_memory": null,
  "driver_cores": null,
  "total_executor_cores": null,
  "executor_cores": null,
  "num_executors": null,
  "should_append_params": false,
  "principal": null,
  "keytab": null,
  "queue": null,
  "yeedu_functions_project_path": null,
  "yeedu_functions_script_path": null,
  "yeedu_functions_function_name": null,
  "yeedu_functions_requirements": null,
  "yeedu_functions_max_request_concurrency": null,
  "yeedu_functions_request_timeout_sec": null,
  "yeedu_functions_idle_timeout_sec": null,
  "yeedu_functions_example_request_body": null,
  "created_by_user_id": "8",
  "modified_by_user_id": "8",
  "last_update_date": "2025-06-26T08:10:29.710Z",
  "from_date": "2025-06-26T08:03:42.948Z",
  "to_date": null
}
```

### enable

```bash
yeedu job enable -h
```

```bash
usage:  enable [-h] --workspace_id WORKSPACE_ID [--job_id JOB_ID] [--job_name JOB_NAME] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to enable the Spark Job.
  --job_id JOB_ID       Provide Job Id to enable the Spark Job.
  --job_name JOB_NAME   Provide Job Name to enable the Spark Job.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- enable example with the required arguments passed.

```bash
yeedu job enable --workspace_id=1 --job_id=1
```

- Console output

```bash
{
  "job_id": "1",
  "job_name": "spark_examples",
  "cluster_id": "1",
  "workspace_id": "1",
  "spark_job_type_lang_id": 1,
  "max_concurrency": "0",
  "job_class_name": "org.apache.spark.examples.SparkPi",
  "job_command": "file:///yeedu/object-storage-manager/spark-examples_2.12-3.2.2.jar",
  "job_arguments": "1000",
  "job_rawScalaCode": null,
  "files": null,
  "properties_file": null,
  "conf": null,
  "packages": null,
  "repositories": null,
  "jars": null,
  "archives": null,
  "driver_memory": null,
  "driver_java_options": null,
  "driver_library_path": null,
  "driver_class_path": null,
  "executor_memory": null,
  "driver_cores": null,
  "total_executor_cores": null,
  "executor_cores": null,
  "num_executors": null,
  "should_append_params": false,
  "principal": null,
  "keytab": null,
  "queue": null,
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T06:37:13.951Z",
  "from_date": "2024-06-14T06:29:47.214Z",
  "to_date": null
}

```

### disable

```bash
yeedu job disable -h
```

```bash
usage:  disable [-h] --workspace_id WORKSPACE_ID [--job_id JOB_ID] [--job_name JOB_NAME] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to disable the Spark Job.
  --job_id JOB_ID       Provide Job Id to disable the Spark Job.
  --job_name JOB_NAME   Provide Job Name to disable the Spark Job.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- disable example with the required arguments passed.

```bash
  yeedu job disable --workspace_id=1 --job_id=1
```

- Console output

```bash
{
  "job_id": "1",
  "job_name": "job_load_test_813cdc68-2ae0-4c8f-8ab7-bcdfe926ee44",
  "cluster_id": "2",
  "workspace_id": "1",
  "spark_job_type_lang_id": 1,
  "max_concurrency": "1",
  "job_class_name": "org.apache.spark.examples.SparkPi",
  "job_command": "/opt/spark/examples/jars/spark-examples_2.12-3.4.3.jar",
  "job_arguments": "1",
  "job_rawScalaCode": null,
  "files": null,
  "properties_file": null,
  "conf": null,
  "packages": null,
  "repositories": null,
  "jars": null,
  "archives": null,
  "driver_memory": null,
  "driver_java_options": null,
  "driver_library_path": null,
  "driver_class_path": null,
  "executor_memory": null,
  "driver_cores": null,
  "total_executor_cores": null,
  "executor_cores": null,
  "num_executors": null,
  "should_append_params": false,
  "principal": null,
  "keytab": null,
  "queue": null,
  "yeedu_functions_project_path": null,
  "yeedu_functions_script_path": null,
  "yeedu_functions_function_name": null,
  "yeedu_functions_requirements": null,
  "yeedu_functions_max_request_concurrency": null,
  "yeedu_functions_request_timeout_sec": null,
  "yeedu_functions_idle_timeout_sec": null,
  "yeedu_functions_example_request_body": null,
  "created_by_user_id": "1",
  "modified_by_user_id": "8",
  "last_update_date": "2025-06-26T08:47:53.066Z",
  "from_date": "2025-05-16T08:39:26.929Z",
  "to_date": "2025-06-26T08:47:53.066Z"
}
```

### export

```bash
yeedu job export -h
```

```bash
usage:  export [-h] --workspace_id WORKSPACE_ID [--job_id JOB_ID]
               [--job_name JOB_NAME] [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to export a specific Spark Job
                        from it.
  --job_id JOB_ID
                        Provide Job Id to export a specific Spark Job
                        Configuration.
  --job_name JOB_NAME
                        Provide Job name to export a specific Spark Job
                        Configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- export example with the required arguments passed.

```bash
yeedu job export --workspace_id=1 --job_id=1
```

- Console output

```bash
{
  "jobs": [
    {
      "job_name": "yeedu_test_job",
      "spark_job_type": {
        "job_type": "SPARK_JOB",
        "language": "Jar"
      },
      "cluster_info": {
        "cluster_name": "aws_test_cluster",
        "cluster_type": "YEEDU"
      },
      "max_concurrency": 0,
      "files": [],
      "properties_file": null,
      "conf": [],
      "packages": [],
      "repositories": [],
      "jars": [],
      "archives": [],
      "driver_memory": null,
      "driver_java_options": "-Dderby.system.home=/yeedu/spark_metastores/1721298078-74183",
      "driver_library_path": null,
      "driver_class_path": null,
      "executor_memory": null,
      "principal": null,
      "keytab": null,
      "queue": null,
      "job_class_name": "org.apache.spark.examples.SparkPi",
      "job_command": "/opt/spark/examples/jars/spark-examples_2.12-3.2.2.jar",
      "job_arguments": "10000",
      "job_rawScalaCode": null,
      "job_timeout_min": 5,
      "driver_cores": null,
      "total_executor_cores": null,
      "executor_cores": null,
      "num_executors": null,
      "should_append_params": false
    }
  ]
}
```

## Spark Job Runs

| Command Name                | Utility                                                                |
| --------------------------- | ---------------------------------------------------------------------- |
| [start](#start)             | To run a Spark Job run.                                                |
| [list-runs](#list-runs)     | To list all the available Spark Job runs.                              |
| [search-runs](#search-runs) | To search Spark Job runs by similar job id.                            |
| [get-run](#get-run)         | To get information about a specific Spark Job run.                     |
| [stop](#stop)               | To stop a specific Spark Job run.                                      |
| [run-status](#run-status)   | To get all the status information about a specific Spark Job run.      |
| [logs](#logs)               | To download Spark Job run logs by run id.                              |

### start

```bash
yeedu job start -h
```

```bash
usage:  start [-h] [--job_id JOB_ID]
              [--job_name JOB_NAME] --workspace_id
              WORKSPACE_ID [--json-output [{pretty,default}]]
              [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --job_id JOB_ID
                        To run a Spark Job run, enter job_id.
  --job_name JOB_NAME
                        To run a Spark Job run, enter job_name.
  --arguments ARGUMENTS
                        Specifies the runtime arguments to run a Spark Job instance.
  --conf CONF
                        Specifies the runtime configurations to run a Spark Job instance.
  --workspace_id WORKSPACE_ID
                        To run a Spark Job run, enter workspace_id.
  --follow   [{true/false}]              
                      Continuously fetch job status until job reaches terminal state (ERROR, STOPPED, DONE, TERMINATED). (default: false)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- start example with one of the required argument passed.

```bash
yeedu job start --workspace_id=1 --job_id=1 
```

- Console output

```bash
{
  "run_id": "1",
  "job_id": "1",
  "cluster_id": "1",
  "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T06:38:03.054Z",
  "from_date": "2024-06-14T06:38:03.054Z",
  "to_date": null
}
```

### list-runs

```bash
yeedu job list-runs -h
```

```bash
usage:  list-runs [-h] --workspace_id WORKSPACE_ID [--cluster_ids [CLUSTER_IDS]]
                  [--job_ids [JOB_IDS]] [--run_status [RUN_STATUS]]
                  [--job_type [JOB_TYPE]] [--job_type_langs [JOB_TYPE_LANGS]]
                  [--created_by_ids [CREATED_BY_IDS]] [--modified_by_ids [MODIFIED_BY_IDS]]
                  [--page_number PAGE_NUMBER] [--limit LIMIT] [--json-output [{pretty,default}]]
                  [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        To list Spark Job runs of a specific workspace_id.
  --cluster_ids [CLUSTER_IDS]
                        To list Spark Job runs for optional set of cluster Ids.
  --job_ids [JOB_IDS]
                        To list Spark Job runs for optional set of Spark job
                        configuration Ids.
  --run_status [RUN_STATUS]
                        To list Spark Job runs for optional set of run_status. Choices
                        are: submitted, running, done, error, terminated, stopping, stopped
  --job_type [JOB_TYPE]
                        To list Spark Job runs for optional set of job_type. Choices
                        are: SPARK_JOB, SPARK_SQL, NOTEBOOK, THRIFT_SQL, YEEDU_FUNCTIONS
  --job_type_langs [JOB_TYPE_LANGS]
                        An optional set of language filter for Spark job runs. Choices
                        are: RAW_SCALA, Jar, Python3, Scala, SQL
  --created_by_ids [CREATED_BY_IDS]
                        To list Spark Job runs for optional set of created by user Ids.
  --modified_by_ids [MODIFIED_BY_IDS]
                        To list Spark Job runs for optional set of modified by user
                        Ids.
  --page_number PAGE_NUMBER
                        To list Spark Job runs for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of job runs. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- list-runs example with required and optional arguments passed.

```bash
yeedu job list-runs --workspace_id=1 --limit=2
```

- Console output

```bash
{
  "data": [
    {
      "run_id": 2,
      "application_id": null,
      "run_status": "RUNNING",
      "total_run_time_sec": 4.499798,
      "execution_time_sec": 2.005716,
      "job_conf": {
        "job_id": 1,
        "job_name": "spark_examples",
        "spark_job_type": {
          "job_type": "SPARK_JOB",
          "language": "Jar"
        },
        "cluster_info": {
          "cluster_id": 1,
          "name": "gcp_test",
          "cluster_status": "RUNNING",
          "cluster_type": "YEEDU",
          "instance_size": 1,
          "min_instances": 1,
          "max_instances": 1,
          "cloud_env": {
            "cloud_env_id": 1,
            "name": "gcp",
            "cloud_provider": {
              "cloud_provider_id": 0,
              "name": "GCP"
            }
          },
          "cluster_conf": {
            "cluster_conf_id": 10,
            "cluster_conf_name": "n1-standard-4",
            "machine_type_category": "general_purpose",
            "machine_type": {
              "machine_type_id": 10,
              "name": "n1-standard-4",
              "vCPUs": 4,
              "memory": "15 GiB",
              "has_cuda": false,
              "gpu_model": null,
              "gpus": 0,
              "gpu_memory": null,
              "cpu_model": [
                "Intel Xeon Scalable (Skylake) 1st Generation",
                "Intel Xeon E5 v4 (Broadwell E5)",
                "Intel Xeon E5 v3 (Haswell)",
                "Intel Xeon E5 v2 (Ivy Bridge)",
                "Intel Xeon E5 (Sandy Bridge)"
              ],
              "cpu_min_frequency_GHz": [
                "2.0",
                "2.2",
                "2.3",
                "2.5",
                "2.6"
              ],
              "cpu_max_frequency_GHz": [
                "3.5",
                "3.7",
                "3.8",
                "3.5",
                "3.6"
              ],
              "has_local_disk": false,
              "local_disk_size_GB": null,
              "local_num_of_disks": null,
              "local_disk_throughput_MB": null,
              "machine_price_ycu": 2.5
            },
            "machine_volume_conf": {
              "volume_conf_id": 2,
              "name": "volume_gcp_2",
              "size": 375,
              "machine_volume_num": 2,
              "machine_volume_strip_num": 2
            }
          },
          "spark_infra_version": {
            "spark_infra_version_id": 1,
            "spark_docker_image_name": "v3.2.2-20",
            "spark_version": "3.2.2",
            "hive_version": "3.2.3",
            "hadoop_version": "3.2.4",
            "scala_version": "2.12.15",
            "python_version": "3.9.5",
            "notebook_support": true,
            "has_cuda_support": true,
            "thrift_support": true,
            "yeedu_functions_support": true
          },
          "engine_cluster_spark_config": {
            "max_parallel_spark_job_execution_per_instance": 5,
            "num_of_workers": null
          }
        }
      },
      "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-06-14T06:39:16.11221+00:00",
      "from_date": "2024-06-14T06:39:16.11221+00:00",
      "to_date": "infinity"
    },
    {
      "run_id": 1,
      "application_id": null,
      "run_status": "ERROR",
      "total_run_time_sec": 5.671385,
      "execution_time_sec": 2.488786,
      "job_conf": {
        "job_id": 1,
        "job_name": "spark_examples",
        "spark_job_type": {
          "job_type": "SPARK_JOB",
          "language": "Jar"
        },
        "cluster_info": {
          "cluster_id": 1,
          "name": "gcp_test",
          "cluster_status": "RUNNING",
          "cluster_type": "YEEDU",
          "instance_size": 1,
          "min_instances": 1,
          "max_instances": 1,
          "cloud_env": {
            "cloud_env_id": 1,
            "name": "gcp",
            "cloud_provider": {
              "cloud_provider_id": 0,
              "name": "GCP"
            }
          },
          "cluster_conf": {
            "cluster_conf_id": 10,
            "cluster_conf_name": "n1-standard-4",
            "machine_type_category": "general_purpose",
            "machine_type": {
              "machine_type_id": 10,
              "name": "n1-standard-4",
              "vCPUs": 4,
              "memory": "15 GiB",
              "has_cuda": false,
              "gpu_model": null,
              "gpus": 0,
              "gpu_memory": null,
              "cpu_model": [
                "Intel Xeon Scalable (Skylake) 1st Generation",
                "Intel Xeon E5 v4 (Broadwell E5)",
                "Intel Xeon E5 v3 (Haswell)",
                "Intel Xeon E5 v2 (Ivy Bridge)",
                "Intel Xeon E5 (Sandy Bridge)"
              ],
              "cpu_min_frequency_GHz": [
                "2.0",
                "2.2",
                "2.3",
                "2.5",
                "2.6"
              ],
              "cpu_max_frequency_GHz": [
                "3.5",
                "3.7",
                "3.8",
                "3.5",
                "3.6"
              ],
              "has_local_disk": false,
              "local_disk_size_GB": null,
              "local_num_of_disks": null,
              "local_disk_throughput_MB": null,
              "machine_price_ycu": 2.5
            },
            "machine_volume_conf": {
              "volume_conf_id": 2,
              "name": "volume_gcp_2",
              "size": 375,
              "machine_volume_num": 2,
              "machine_volume_strip_num": 2
            }
          },
          "spark_infra_version": {
            "spark_infra_version_id": 1,
            "spark_docker_image_name": "v3.2.2-20",
            "spark_version": "3.2.2",
            "hive_version": "3.2.3",
            "hadoop_version": "3.2.4",
            "scala_version": "2.12.15",
            "python_version": "3.9.5",
            "notebook_support": true,
            "has_cuda_support": true,
            "thrift_support": true,
            "yeedu_functions_support": true
          },
          "engine_cluster_spark_config": {
            "max_parallel_spark_job_execution_per_instance": 5,
            "num_of_workers": null
          }
        }
      },
      "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-06-14T06:38:03.054482+00:00",
      "from_date": "2024-06-14T06:38:03.054482+00:00",
      "to_date": "2024-06-14T06:38:08.725867+00:00"
    }
  ]
}
```

- list-runs example to list spark jobs of a particular workspace having specific spark job status.

```bash
yeedu job list-runs --workspace_id=1 --run_status=done --limit=1
```

- Console output

```bash
{
  "data": [
    {
      "run_id": 1,
      "application_id": "local-1718347762051",
      "run_status": "DONE",
      "total_run_time_sec": 25.057991,
      "execution_time_sec": 22.512167,
      "job_conf": {
        "job_id": 1,
        "job_name": "spark_examples",
        "spark_job_type": {
          "job_type": "SPARK_JOB",
          "language": "Jar"
        },
        "cluster_info": {
          "cluster_id": 1,
          "name": "gcp_test",
          "cluster_status": "RUNNING",
          "cluster_type": "YEEDU",
          "instance_size": 1,
          "min_instances": 1,
          "max_instances": 1,
          "cloud_env": {
            "cloud_env_id": 1,
            "name": "gcp",
            "cloud_provider": {
              "cloud_provider_id": 0,
              "name": "GCP"
            }
          },
          "cluster_conf": {
            "cluster_conf_id": 10,
            "cluster_conf_name": "n1-standard-4",
            "machine_type_category": "general_purpose",
            "machine_type": {
              "machine_type_id": 10,
              "name": "n1-standard-4",
              "vCPUs": 4,
              "memory": "15 GiB",
              "has_cuda": false,
              "gpu_model": null,
              "gpus": 0,
              "gpu_memory": null,
              "cpu_model": [
                "Intel Xeon Scalable (Skylake) 1st Generation",
                "Intel Xeon E5 v4 (Broadwell E5)",
                "Intel Xeon E5 v3 (Haswell)",
                "Intel Xeon E5 v2 (Ivy Bridge)",
                "Intel Xeon E5 (Sandy Bridge)"
              ],
              "cpu_min_frequency_GHz": [
                "2.0",
                "2.2",
                "2.3",
                "2.5",
                "2.6"
              ],
              "cpu_max_frequency_GHz": [
                "3.5",
                "3.7",
                "3.8",
                "3.5",
                "3.6"
              ],
              "has_local_disk": false,
              "local_disk_size_GB": null,
              "local_num_of_disks": null,
              "local_disk_throughput_MB": null,
              "machine_price_ycu": 2.5
            },
            "machine_volume_conf": {
              "volume_conf_id": 2,
              "name": "volume_gcp_2",
              "size": 375,
              "machine_volume_num": 2,
              "machine_volume_strip_num": 2
            }
          },
          "spark_infra_version": {
            "spark_infra_version_id": 1,
            "spark_docker_image_name": "v3.2.2-20",
            "spark_version": "3.2.2",
            "hive_version": "3.2.3",
            "hadoop_version": "3.2.4",
            "scala_version": "2.12.15",
            "python_version": "3.9.5",
            "notebook_support": true,
            "has_cuda_support": true,
            "thrift_support": true,
            "yeedu_functions_support": true
          },
          "engine_cluster_spark_config": {
            "max_parallel_spark_job_execution_per_instance": 5,
            "num_of_workers": null
          }
        }
      },
      "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-06-14T06:49:16.511361+00:00",
      "from_date": "2024-06-14T06:49:16.511361+00:00",
      "to_date": "2024-06-14T06:49:41.569352+00:00"
    }
  ]
}
```

### search-runs

```bash
yeedu job search-runs -h
```

```bash
usage:  search-runs [-h] --workspace_id WORKSPACE_ID --job_name JOB_NAME
                    [--cluster_ids [CLUSTER_IDS]] [--run_status [RUN_STATUS]]
                    [--job_type [JOB_TYPE]] [--job_type_langs [JOB_TYPE_LANGS]]
                    [--created_by_ids [CREATED_BY_IDS]] [--modified_by_ids [MODIFIED_BY_IDS]]
                    [--page_number PAGE_NUMBER] [--limit LIMIT]
                    [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to search Spark Job runs in it.
  --job_name JOB_NAME
                        To search Spark Job runs of a specific job_name.
  --cluster_ids [CLUSTER_IDS]
                        To search Spark Job runs for optional set of cluster Ids.
  --run_status [RUN_STATUS]
                        To search Spark Job runs for optional set of run_status.
                        Choices are: submitted, running, done, error, terminated, stopping,
                        stopped
  --job_type [JOB_TYPE]
                        To search Spark Job runs for optional set of job_type. Choices
                        are: SPARK_JOB, SPARK_SQL, NOTEBOOK, THRIFT_SQL, YEEDU_FUNCTIONS
  --job_type_langs [JOB_TYPE_LANGS]
                        An optional set of language filter for Spark job runs. Choices
                        are: RAW_SCALA, Jar, Python3, Scala, SQL
  --created_by_ids [CREATED_BY_IDS]
                        To search Spark Job runs for optional set of created by user
                        Ids.
  --modified_by_ids [MODIFIED_BY_IDS]
                        To search Spark Job runs for optional set of modified by user
                        Ids.
  --page_number PAGE_NUMBER
                        To search Spark Job runs for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of Spark Job runs. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- search-runs example with required and optional arguments passed.

```bash
yeedu job search-runs --workspace_id=1 --job_name=spark_examples --limit=1
```

- Console output

```bash
{
  "data": [
    {
      "run_id": 1,
      "application_id": "local-1718347762051",
      "run_status": "DONE",
      "total_run_time_sec": 25.057991,
      "execution_time_sec": 22.512167,
      "job_conf": {
        "job_id": 1,
        "name": "spark_examples",
        "spark_job_type": {
          "job_type": "SPARK_JOB",
          "language": "Jar"
        },
        "cluster_info": {
          "cluster_id": 1,
          "name": "gcp_test",
          "cluster_status": "RUNNING",
          "cluster_type": "YEEDU",
          "instance_size": 1,
          "min_instances": 1,
          "max_instances": 1,
          "cloud_env": {
            "cloud_env_id": 1,
            "name": "gcp",
            "cloud_provider": {
              "cloud_provider_id": 0,
              "name": "GCP"
            }
          },
          "cluster_conf": {
            "cluster_conf_id": 10,
            "cluster_conf_name": "n1-standard-4",
            "machine_type_category": "general_purpose",
            "machine_type": {
              "machine_type_id": 10,
              "name": "n1-standard-4",
              "vCPUs": 4,
              "memory": "15 GiB",
              "has_cuda": false,
              "gpu_model": null,
              "gpus": 0,
              "gpu_memory": null,
              "cpu_model": [
                "Intel Xeon Scalable (Skylake) 1st Generation",
                "Intel Xeon E5 v4 (Broadwell E5)",
                "Intel Xeon E5 v3 (Haswell)",
                "Intel Xeon E5 v2 (Ivy Bridge)",
                "Intel Xeon E5 (Sandy Bridge)"
              ],
              "cpu_min_frequency_GHz": [
                "2.0",
                "2.2",
                "2.3",
                "2.5",
                "2.6"
              ],
              "cpu_max_frequency_GHz": [
                "3.5",
                "3.7",
                "3.8",
                "3.5",
                "3.6"
              ],
              "has_local_disk": false,
              "local_disk_size_GB": null,
              "local_num_of_disks": null,
              "local_disk_throughput_MB": null,
              "machine_price_ycu": 2.5
            },
            "machine_volume_conf": {
              "volume_conf_id": 2,
              "name": "volume_gcp_2",
              "size": 375,
              "machine_volume_num": 2,
              "machine_volume_strip_num": 2
            }
          },
          "spark_infra_version": {
            "spark_infra_version_id": 1,
            "spark_docker_image_name": "v3.2.2-20",
            "spark_version": "3.2.2",
            "hive_version": "3.2.3",
            "hadoop_version": "3.2.4",
            "scala_version": "2.12.15",
            "python_version": "3.9.5",
            "notebook_support": true,
            "has_cuda_support": true,
            "thrift_support": true,
            "yeedu_functions_support": true
          },
          "engine_cluster_spark_config": {
            "max_parallel_spark_job_execution_per_instance": 5,
            "num_of_workers": null
          }
        }
      },
      "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-06-14T06:49:16.511361+00:00",
      "from_date": "2024-06-14T06:49:16.511361+00:00",
      "to_date": "2024-06-14T06:49:41.569352+00:00"
    }
  ]
}
```

### get-run

```bash
yeedu job get-run -h
```

```bash
usage:  get-run [-h] --run_id RUN_ID --workspace_id WORKSPACE_ID
                [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --run_id RUN_ID       Provide run_id to get information about a specific Spark Job
                        Instance.
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to get information about a specific Spark
                        Job run.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-run example with all the required arguments passed.

```bash
yeedu job get-run --workspace_id=1 --run_id=4
```

- Console output

```bash
{
  "run_id": 4,
  "application_id": "local-1718347762051",
  "run_status": "DONE",
  "execution_time_sec": 22.512167,
  "total_run_time_sec": 25.057991,
  "job_conf": {
    "job_id": 1,
    "job_name": "spark_examples",
    "spark_job_type": {
      "job_type": "SPARK_JOB",
      "language": "Jar"
    },
    "cluster_info": {
      "cluster_id": 1,
      "name": "gcp_test",
      "cluster_status": "RUNNING",
      "cluster_type": "YEEDU",
      "instance_size": 1,
      "min_instances": 1,
      "max_instances": 1,
      "cloud_env": {
        "cloud_env_id": 1,
        "name": "gcp",
        "cloud_provider": {
          "cloud_provider_id": 0,
          "name": "GCP"
        }
      },
      "cluster_conf": {
        "cluster_conf_id": 10,
        "cluster_conf_name": "n1-standard-4",
        "machine_type_category": "general_purpose",
        "machine_type": {
          "machine_type_id": 10,
          "name": "n1-standard-4",
          "vCPUs": 4,
          "memory": "15 GiB",
          "has_cuda": false,
          "gpu_model": null,
          "gpus": 0,
          "gpu_memory": null,
          "cpu_model": [
            "Intel Xeon Scalable (Skylake) 1st Generation",
            "Intel Xeon E5 v4 (Broadwell E5)",
            "Intel Xeon E5 v3 (Haswell)",
            "Intel Xeon E5 v2 (Ivy Bridge)",
            "Intel Xeon E5 (Sandy Bridge)"
          ],
          "cpu_min_frequency_GHz": [
            "2.0",
            "2.2",
            "2.3",
            "2.5",
            "2.6"
          ],
          "cpu_max_frequency_GHz": [
            "3.5",
            "3.7",
            "3.8",
            "3.5",
            "3.6"
          ],
          "has_local_disk": false,
          "local_disk_size_GB": null,
          "local_num_of_disks": null,
          "local_disk_throughput_MB": null,
          "machine_price_ycu": 2.5
        },
        "machine_volume_conf": {
          "volume_conf_id": 2,
          "name": "volume_gcp_2",
          "size": 375,
          "machine_volume_num": 2,
          "machine_volume_strip_num": 2
        }
      },
      "spark_infra_version": {
        "spark_infra_version_id": 1,
        "spark_docker_image_name": "v3.2.2-20",
        "spark_version": "3.2.2",
        "hive_version": "3.2.3",
        "hadoop_version": "3.2.4",
        "scala_version": "2.12.15",
        "python_version": "3.9.5",
        "notebook_support": true,
        "has_cuda_support": true,
        "thrift_support": true,
        "yeedu_functions_support": true
      },
      "engine_cluster_spark_config": {
        "max_parallel_spark_job_execution_per_instance": 5,
        "num_of_workers": null
      }
    }
  },
  "workflow_job_instance_details": {
    "workflow_job_instance_status": {
      "workflow_job_instance_id": 5,
      "workflow_job_id": 5,
      "status": "DONE",
      "from_date": "2024-06-14T06:49:16.511361+00:00",
      "to_date": "2024-06-14T06:49:41.569352+00:00"
    },
    "workflow_execution_process": {
      "machine_pid_number": "425",
      "machine_hostname": "yeedu1-bcd2b294-deb1-10c9-0b8e-8e471e5c46f3",
      "machine_id": "bcd2b294-deb1-10c9-0b8e-8e471e5c46f3",
      "machine_pid_user": "root",
      "machine_node_number": "0"
    }
  },
  "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
  "created_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "last_update_date": "2024-06-14T06:49:16.511361+00:00",
  "from_date": "2024-06-14T06:49:16.511361+00:00",
  "to_date": "2024-06-14T06:49:41.569352+00:00"
}
```

### stop

```bash
yeedu job stop -h
```

```bash
usage:  stop [-h] --run_id RUN_ID --workspace_id WORKSPACE_ID
             [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --run_id RUN_ID       Provide run_id to stop a specific Spark Job run.
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to stop a specific Spark Job run.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- stop example with all the required argument passed.

```bash
yeedu job stop --workspace_id=1 --run_id=5
```

- Console output

```bash
{
  "SparkKill": {
    "workflow_job_id": 6,
    "workflow_job_instance_id": 6,
    "spark_job_instance_id": 5,
    "spark_job_id": 1,
    "compute_engine_id": 1
  }
}
```

### run-status

```bash
yeedu job run-status -h
```

```bash
usage:  run-status [-h] --run_id RUN_ID --workspace_id WORKSPACE_ID
                   [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --run_id RUN_ID       Provide run_id to get all the status information about a
                        specific Spark Job run.
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to get all the status information about a
                        specific Spark Job run.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- run-status example with all the required argument passed.

```bash
yeedu job run-status --workspace_id=1 --run_id=5
```

- Console output

```bash
[
  {
    "run_status": "SUBMITTED",
    "created_by": "YSU0000",
    "start_time": "2024-06-14T06:49:16.511361+00:00",
    "end_time": "2024-06-14T06:49:19.057185+00:00"
  },
  {
    "run_status": "RUNNING",
    "created_by": "YSU0000",
    "start_time": "2024-06-14T06:49:19.057185+00:00",
    "end_time": "2024-06-14T06:49:41.569352+00:00"
  },
  {
    "run_status": "DONE",
    "created_by": "YSU0000",
    "start_time": "2024-06-14T06:49:41.569352+00:00",
    "end_time": "infinity"
  }
]
```

### logs

```bash
yeedu job logs -h
```

```bash
usage:  logs [-h] --workspace_id WORKSPACE_ID --run_id RUN_ID [--log_type {stdout,stderr}] [--last_n_lines LAST_N_LINES] [--file_size_bytes FILE_SIZE_BYTES] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to download Spark Job run log records.
  --run_id RUN_ID       Provide run_id to download Spark Job run log records.
  --log_type {stdout,stderr}
                        Provide log_type to download Spark Job run log records. (default: stdout)
  --last_n_lines LAST_N_LINES
                        Number of lines to retrieve from the end of the log file (sample preview).
  --file_size_bytes FILE_SIZE_BYTES
                        Number of bytes to preview from the beginning of the log file (sample preview).
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- logs example with all the required arguments passed.

```bash
yeedu job logs --workspace_id=1 --run_id=4
```

- Console output

```bash
Pi is roughly 3.141355706778534
```
{
  "run_id": 4,
  "application_id": "local-1718347762051",
  "run_status": "DONE",
  "compute_engine": 1,
  "cluster_id": "1",
  "workflow_job_instance_details": {
    "workflow_job_instance_status": {
      "workflow_job_instance_id": 5,
      "workflow_job_id": 5,
      "status": "DONE",
      "previous_status": [
        "NONE",
        "INIT",
        "SENT",
        "RECEIVED",
        "EXECUTING"
      ],
      "from_date": "2024-06-14T06:49:41.569352+00:00",
      "to_date": "infinity"
    },
    "workflow_execution_process": {
      "machine_pid_number": "425",
      "machine_hostname": "yeedu1-bcd2b294-deb1-10c9-0b8e-8e471e5c46f3",
      "machine_id": "bcd2b294-deb1-10c9-0b8e-8e471e5c46f3",
      "machine_pid_user": "root",
      "machine_node_number": "0"
    }
  },
  "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
  "created_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "last_update_date": "2024-06-14T06:49:16.511361+00:00",
  "from_date": "2024-06-14T06:49:16.511361+00:00",
  "to_date": "2024-06-14T06:49:41.569352+00:00"
}
```

## Workflow Details By Spark Job Application ID

| Command Name                                            | Utility                                                    |
| ------------------------------------------------------- | ---------------------------------------------------------- |
| [get-workflow-job-instance](#get-workflow-job-instance) | To get information about a specific Workflow Job run.      |

### get-workflow-job-instance

```bash
yeedu job get-workflow-job-instance -h
```

```bash
usage:  get-workflow-job-instance [-h] --application_id APPLICATION_ID
                                  --workspace_id WORKSPACE_ID
                                  [--json-output [{pretty,default}]]
                                  [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --application_id APPLICATION_ID
                        Provide a application_id to get information about a specific
                        Workflow Job run.
  --workspace_id WORKSPACE_ID
                        Provide a workspace_id to get information about a specific
                        Workflow Job run.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-workflow-job-instance example with all the required arguments passed.

```bash
yeedu job get-workflow-job-instance --workspace_id=1 --application_id=local-1718347762051
```

- Console output

```bash
{
  "run_id": 4,
  "application_id": "local-1718347762051",
  "run_status": "DONE",
  "compute_engine": 1,
  "cluster_id": "1",
  "workflow_job_instance_details": {
    "workflow_job_instance_status": {
      "workflow_job_instance_id": 5,
      "workflow_job_id": 5,
      "status": "DONE",
      "previous_status": [
        "NONE",
        "INIT",
        "SENT",
        "RECEIVED",
        "EXECUTING"
      ],
      "from_date": "2024-06-14T06:49:41.569352+00:00",
      "to_date": "infinity"
    },
    "workflow_execution_process": {
      "machine_pid_number": "425",
      "machine_hostname": "yeedu1-bcd2b294-deb1-10c9-0b8e-8e471e5c46f3",
      "machine_id": "bcd2b294-deb1-10c9-0b8e-8e471e5c46f3",
      "machine_pid_user": "root",
      "machine_node_number": "0"
    }
  },
  "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
  "created_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "last_update_date": "2024-06-14T06:49:16.511361+00:00",
  "from_date": "2024-06-14T06:49:16.511361+00:00",
  "to_date": "2024-06-14T06:49:41.569352+00:00"
}
```

# Notebook

## Notebook

| Command Name                    | Utility                                                            |
| ------------------------------- | ------------------------------------------------------------------ |
| [create](#create-3)             | To create a Notebook.                                              |
| [list](#list-3)                 | To list all the available Notebooks.                               |
| [search](#search-3)             | To search Notebooks by notebook name in a workspace.               |
| [get](#get-3)                   | To get the information about a specific Notebook.                  |
| [edit](#edit-3)                 | To edit the Notebook.                                              |
| [enable](#enable-3)             | To enable a specific Notebook.                                     |
| [disable](#disable-3)           | To disable a specific Notebook.                                    |
| [export](#export-2)             | Export a specific Notebook.                                        |
| [clone](#clone)                 | To clone a Notebook.                                               |

### create

```bash
yeedu notebook create -h
```

```bash
usage:  create [-h] --workspace_id WORKSPACE_ID
                    [--cluster_id CLUSTER_ID]
                    [--cluster_name CLUSTER_NAME] --notebook_name
                    NOTEBOOK_NAME --notebook_type python3,scala
                    [--notebook_path NOTEBOOK_PATH]
                    [--conf CONF [CONF ...]] [--files [FILES]]
                    [--jars [JARS]] [--packages [PACKAGES]]
                    [--driver-memory [DRIVER_MEMORY]]
                    [--executor-memory [EXECUTOR_MEMORY]]
                    [--driver-cores [DRIVER_CORES]]
                    [--total-executor-cores [TOTAL_EXECUTOR_CORES]]
                    [--executor-cores [EXECUTOR_CORES]]
                    [--num-executors [NUM_EXECUTORS]]
                    [--should_append_params [should_append_params]]
                    [--json-output [{pretty,default}]]
                    [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to create a Notebook.
  --cluster_id CLUSTER_ID
                        Provide cluster_id to create a Notebook.
  --cluster_name CLUSTER_NAME
                        Provide cluster_name to create a Notebook.
  --notebook_name NOTEBOOK_NAME
                        Provide notebook_name to create a Notebook.
  --notebook_type python3,scala,sql
                        Provide notebook type to create a Notebook.
  --notebook_path NOTEBOOK_PATH
                        Provide notebook_path to create a Notebook.
  --conf CONF [CONF ...]
                        Provide conf to create a Notebook.
  --files [FILES]       Provide files to create a Notebook.
  --jars [JARS]         Provide jars to create a Notebook.
  --packages [PACKAGES]
                        Provide packages to create a Notebook.
  --driver-memory [DRIVER_MEMORY]
                        Provide driver-memory to create a Notebook.
  --executor-memory [EXECUTOR_MEMORY]
                        Provide executor-memory to create a Notebook.
  --driver-cores [DRIVER_CORES]
                        Provide driver-cores to create a Notebook.
  --total-executor-cores [TOTAL_EXECUTOR_CORES]
                        Provide total-executor-cores to create a Notebook.
  --executor-cores [EXECUTOR_CORES]
                        Provide executor-cores to create a Notebook.
  --num-executors [NUM_EXECUTORS]
                        Provide num-executors to create a Notebook.
  --should_append_params [should_append_params]
                        Determines whether the job-level Spark configuration should append to or override the cluster-level Spark configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create example with all the required and optional arguments passed.

```bash
yeedu notebook create --cluster_id=1 --workspace_id=1 --notebook_name="test_notebook" --notebook_type="python3"
```

- Console output

```bash
{
  "notebook_id": "2",
  "notebook_name": "test_notebook",
  "cluster_id": "1",
  "workspace_id": "1",
  "spark_job_type_lang_id": 3,
  "max_concurrency": "1",
  "notebook_file_id": "1",
  "notebook_cells_auto_save": null,
  "conf": null,
  "packages": null,
  "jars": null,
  "files": null,
  "driver_memory": null,
  "executor_memory": null,
  "driver_cores": null,
  "total_executor_cores": null,
  "executor_cores": null,
  "num_executors": null,
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T07:05:31.507Z",
  "from_date": "2024-06-14T07:05:31.507Z",
  "to_date": null
}
```

### list

```bash
yeedu notebook list -h
```

```bash
usage:  list [-h] --workspace_id WORKSPACE_ID [--enable [{true,false}]]
                   [--cluster_ids [CLUSTER_IDS]] [--language [LANGUAGE]]
                   [--last_run_status [LAST_RUN_STATUS]] [--created_by_ids [CREATED_BY_IDS]]
                   [--modified_by_ids [MODIFIED_BY_IDS]] [--page_number PAGE_NUMBER]
                   [--limit LIMIT] [--json-output [{pretty,default}]]
                   [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        To list Notebooks of a specific workspace.
  --enable [{true,false}]
                        Provide enable as true or false to list Notebooks of a specific workspace.
  --cluster_ids [CLUSTER_IDS]
                        An optional set of cluster instance IDs to filter on.
  --language [LANGUAGE]
                        An optional set of language filter for notebooks. Choices are: Python3, Scala, SQL
  --last_run_status [LAST_RUN_STATUS]
                        An optional set of last run statuses to filter notebooks. Choices are: submitted, running, done, error, terminated, stopping, stopped
  --created_by_ids [CREATED_BY_IDS]
                        An optional set of created by user IDs to filter on.
  --modified_by_ids [MODIFIED_BY_IDS]
                        An optional set of modified by user IDs to filter on.
  --page_number PAGE_NUMBER
                        To list Notebooks for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of Notebooks. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- list example with required and optional arguments passed.

```bash
yeedu notebook list --workspace_id=1 --limit=1
```

- Console output

```bash
{
  "data": [
    {
      "notebook_id": 2,
      "notebook_name": "test_notebook",
      "spark_job_type": {
        "job_type": "NOTEBOOK",
        "language": "Python3"
      },
      "cluster_info": {
        "cluster_id": 1,
        "name": "gcp_test",
        "cluster_status": "RUNNING",
        "cluster_type": "YEEDU",
        "instance_size": 1,
        "min_instances": 1,
        "max_instances": 1,
        "cloud_env": {
          "cloud_env_id": 1,
          "name": "gcp",
          "cloud_provider": {
            "cloud_provider_id": 0,
            "name": "GCP"
          }
        },
        "cluster_conf": {
          "cluster_conf_id": 10,
          "cluster_conf_name": "n1-standard-4",
          "machine_type_category": "general_purpose",
          "machine_type": {
            "machine_type_id": 10,
            "name": "n1-standard-4",
            "vCPUs": 4,
            "memory": "15 GiB",
            "has_cuda": false,
            "gpu_model": null,
            "gpus": 0,
            "gpu_memory": null,
            "cpu_model": [
              "Intel Xeon Scalable (Skylake) 1st Generation",
              "Intel Xeon E5 v4 (Broadwell E5)",
              "Intel Xeon E5 v3 (Haswell)",
              "Intel Xeon E5 v2 (Ivy Bridge)",
              "Intel Xeon E5 (Sandy Bridge)"
            ],
            "cpu_min_frequency_GHz": [
              "2.0",
              "2.2",
              "2.3",
              "2.5",
              "2.6"
            ],
            "cpu_max_frequency_GHz": [
              "3.5",
              "3.7",
              "3.8",
              "3.5",
              "3.6"
            ],
            "has_local_disk": false,
            "local_disk_size_GB": null,
            "local_num_of_disks": null,
            "local_disk_throughput_MB": null,
            "machine_price_ycu": 2.5
          },
          "machine_volume_conf": {
            "volume_conf_id": 2,
            "name": "volume_gcp_2",
            "size": 375,
            "machine_volume_num": 2,
            "machine_volume_strip_num": 2
          }
        },
        "spark_infra_version": {
          "spark_infra_version_id": 1,
          "spark_docker_image_name": "v3.2.2-20",
          "spark_version": "3.2.2",
          "hive_version": "3.2.3",
          "hadoop_version": "3.2.4",
          "scala_version": "2.12.15",
          "python_version": "3.9.5",
          "notebook_support": true,
          "has_cuda_support": true,
          "thrift_support": true,
          "yeedu_functions_support": true
        },
        "engine_cluster_spark_config": {
          "max_parallel_spark_job_execution_per_instance": 5,
          "num_of_workers": null
        }
      },
      "last_notebook_run": {
        "run_id": null,
        "run_status": null
      },
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-06-14T07:05:31.507399+00:00",
      "from_date": "2024-06-14T07:05:31.507399+00:00",
      "to_date": "infinity"
    }
  ]
}
```

### search

```bash
yeedu notebook search -h
```

```bash
usage:  search [-h] --workspace_id WORKSPACE_ID --notebook_name NOTEBOOK_NAME
                     [--enable [{true,false}]] [--cluster_ids [CLUSTER_IDS]]
                     [--language [LANGUAGE]] [--last_run_status [LAST_RUN_STATUS]]
                     [--created_by_ids [CREATED_BY_IDS]]
                     [--modified_by_ids [MODIFIED_BY_IDS]] [--page_number PAGE_NUMBER]
                     [--limit LIMIT] [--json-output [{pretty,default}]]
                     [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to search Notebooks in it.
  --notebook_name NOTEBOOK_NAME
                        Provide notebook_name to search Notebooks.
  --enable [{true,false}]
                        Provide enable as true or false to search Notebooks.
  --cluster_ids [CLUSTER_IDS]
                        An optional set of cluster instance IDs to filter on.
  --language [LANGUAGE]
                        An optional set of language filter for notebooks.
                        Choices are: Python3, Scala
  --last_run_status [LAST_RUN_STATUS]
                        An optional set of last run statuses to filter notebook
                        configurations. Choices are: submitted, running, done, error,
                        terminated, stopping, stopped
  --created_by_ids [CREATED_BY_IDS]
                        An optional set of created by user IDs to filter on.
  --modified_by_ids [MODIFIED_BY_IDS]
                        An optional set of modified by user IDs to filter on.
  --page_number PAGE_NUMBER
                        To search Notebooks for a specific page_number.
                        (default: 1)
  --limit LIMIT         Provide limit to search number of Notebooks.
                        (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- search example with required and optional arguments passed.

```bash
yeedu notebook search --workspace_id=1 --notebook_name="test_" --enable=true --limit=1
```

- Console output

```bash
{
  "data": [
    {
      "notebook_id": 2,
      "notebook_name": "test_notebook",
      "spark_job_type": {
        "job_type": "NOTEBOOK",
        "language": "Python3"
      },
      "cluster_info": {
        "cluster_id": 1,
        "name": "gcp_test",
        "cluster_status": "RUNNING",
        "cluster_type": "YEEDU",
        "instance_size": 1,
        "min_instances": 1,
        "max_instances": 1,
        "cloud_env": {
          "cloud_env_id": 1,
          "name": "gcp",
          "cloud_provider": {
            "cloud_provider_id": 0,
            "name": "GCP"
          }
        },
        "cluster_conf": {
          "cluster_conf_id": 10,
          "cluster_conf_name": "n1-standard-4",
          "machine_type_category": "general_purpose",
          "machine_type": {
            "machine_type_id": 10,
            "name": "n1-standard-4",
            "vCPUs": 4,
            "memory": "15 GiB",
            "has_cuda": false,
            "gpu_model": null,
            "gpus": 0,
            "gpu_memory": null,
            "cpu_model": [
              "Intel Xeon Scalable (Skylake) 1st Generation",
              "Intel Xeon E5 v4 (Broadwell E5)",
              "Intel Xeon E5 v3 (Haswell)",
              "Intel Xeon E5 v2 (Ivy Bridge)",
              "Intel Xeon E5 (Sandy Bridge)"
            ],
            "cpu_min_frequency_GHz": [
              "2.0",
              "2.2",
              "2.3",
              "2.5",
              "2.6"
            ],
            "cpu_max_frequency_GHz": [
              "3.5",
              "3.7",
              "3.8",
              "3.5",
              "3.6"
            ],
            "has_local_disk": false,
            "local_disk_size_GB": null,
            "local_num_of_disks": null,
            "local_disk_throughput_MB": null,
            "machine_price_ycu": 2.5
          },
          "machine_volume_conf": {
            "volume_conf_id": 2,
            "name": "volume_gcp_2",
            "size": 375,
            "machine_volume_num": 2,
            "machine_volume_strip_num": 2
          }
        },
        "spark_infra_version": {
          "spark_infra_version_id": 1,
          "spark_docker_image_name": "v3.2.2-20",
          "spark_version": "3.2.2",
          "hive_version": "3.2.3",
          "hadoop_version": "3.2.4",
          "scala_version": "2.12.15",
          "python_version": "3.9.5",
          "notebook_support": true,
          "has_cuda_support": true,
          "thrift_support": true,
          "yeedu_functions_support": true
        },
        "engine_cluster_spark_config": {
          "max_parallel_spark_job_execution_per_instance": 5,
          "num_of_workers": null
        }
      },
      "last_notebook_run": {
        "run_id": null,
        "run_status": null
      },
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-06-14T07:05:31.507399+00:00",
      "from_date": "2024-06-14T07:05:31.507399+00:00",
      "to_date": "infinity"
    }
  ]
}
```

### get

```bash
yeedu notebook get -h
```

```bash
usage:  get [-h] --workspace_id WORKSPACE_ID [--notebook_id NOTEBOOK_ID]
                 [--notebook_name NOTEBOOK_NAME] [--json-output [{pretty,default}]]
                 [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to get information about a specific Notebook
                        Configuration.
  --notebook_id NOTEBOOK_ID
                        Provide Notebook Conf Id to get information about a specific
                        Notebook.
  --notebook_name NOTEBOOK_NAME
                        Provide Notebook Name to get information about a specific Notebook
                        Configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- get example with the optional and required arguments passed.

```bash
yeedu notebook get --workspace_id=1 --notebook_id=2
```

- Console output

```bash
{
  "notebook_id": 2,
  "notebook_name": "test_notebook",
  "cluster_info": {
    "cluster_id": 1,
    "name": "gcp_test",
    "cluster_status": "RUNNING",
    "cluster_type": "YEEDU",
    "instance_size": 1,
    "min_instances": 1,
    "max_instances": 1,
    "cluster_conf": {
      "cluster_conf_id": 10,
      "cluster_conf_name": "n1-standard-4",
      "machine_type_category": "general_purpose",
      "machine_type": {
        "machine_type_id": 10,
        "name": "n1-standard-4",
        "vCPUs": 4,
        "memory": "15 GiB",
        "has_cuda": false,
        "gpu_model": null,
        "gpus": 0,
        "gpu_memory": null,
        "cpu_model": [
          "Intel Xeon Scalable (Skylake) 1st Generation",
          "Intel Xeon E5 v4 (Broadwell E5)",
          "Intel Xeon E5 v3 (Haswell)",
          "Intel Xeon E5 v2 (Ivy Bridge)",
          "Intel Xeon E5 (Sandy Bridge)"
        ],
        "cpu_min_frequency_GHz": [
          "2.0",
          "2.2",
          "2.3",
          "2.5",
          "2.6"
        ],
        "cpu_max_frequency_GHz": [
          "3.5",
          "3.7",
          "3.8",
          "3.5",
          "3.6"
        ],
        "has_local_disk": false,
        "local_disk_size_GB": null,
        "local_num_of_disks": null,
        "local_disk_throughput_MB": null,
        "machine_price_ycu": 2.5
      },
      "machine_volume_conf": {
        "volume_conf_id": 2,
        "name": "volume_gcp_2",
        "size": 375,
        "machine_volume_num": 2,
        "machine_volume_strip_num": 2
      }
    },
    "cloud_env": {
      "cloud_env_id": 1,
      "name": "gcp",
      "cloud_provider": {
        "cloud_provider_id": 0,
        "name": "GCP"
      }
    },
    "spark_infra_version": {
      "spark_infra_version_id": 1,
      "spark_docker_image_name": "v3.2.2-20",
      "spark_version": "3.2.2",
      "hive_version": "3.2.3",
      "hadoop_version": "3.2.4",
      "scala_version": "2.12.15",
      "python_version": "3.9.5",
      "notebook_support": true,
      "has_cuda_support": true,
      "thrift_support": true,
      "yeedu_functions_support": true
    },
    "engine_cluster_spark_config": {
      "max_parallel_spark_job_execution_per_instance": 5,
      "num_of_workers": null
    }
  },
  "spark_job_type": {
    "job_type": "NOTEBOOK",
    "language": "Python3"
  },
  "max_concurrency": 1,
  "notebook_file_id": 1,
  "files": null,
  "conf": null,
  "packages": null,
  "jars": null,
  "driver_memory": null,
  "driver_java_options": null,
  "driver_library_path": null,
  "driver_class_path": null,
  "executor_memory": null,
  "driver_cores": null,
  "total_executor_cores": null,
  "executor_cores": null,
  "num_executors": null,
  "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
  "created_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "last_update_date": "2024-06-14T07:05:31.507399+00:00",
  "from_date": "2024-06-14T07:05:31.507399+00:00",
  "to_date": "infinity"
}
```

### edit

```bash
yeedu notebook edit -h
```

```bash
usage:  edit [-h] --workspace_id WORKSPACE_ID
                  [--notebook_id NOTEBOOK_ID]
                  [--notebook_name NOTEBOOK_NAME]
                  [--cluster_id CLUSTER_ID]
                  [--cluster_name CLUSTER_NAME] [--name [NAME]]
                  [--conf CONF [CONF ...]] [--files [FILES]]
                  [--jars [JARS]] [--packages [PACKAGES]]
                  [--driver-memory [DRIVER_MEMORY]]
                  [--executor-memory [EXECUTOR_MEMORY]]
                  [--driver-cores [DRIVER_CORES]]
                  [--total-executor-cores [TOTAL_EXECUTOR_CORES]]
                  [--executor-cores [EXECUTOR_CORES]]
                  [--num-executors [NUM_EXECUTORS]]
                  [--should_append_params [should_append_params]]
                  [--json-output [{pretty,default}]]
                  [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to edit a Notebook.
  --notebook_id NOTEBOOK_ID
                        Provide Notbeook Conf Id to edit a Notebook.
  --notebook_name NOTEBOOK_NAME
                        Provide Notebook Name to edit a Notebook.
  --cluster_id CLUSTER_ID
                        Provide cluster_id to edit a Notebook.
  --cluster_name CLUSTER_NAME
                        Provide cluster_name to edit a Notebook.
  --name [NAME]         Provide name to edit notebook_name of a Notebook.
  --conf CONF [CONF ...]
                        Provide conf to edit a Notebook.
  --files [FILES]       Provide files to edit a Notebook.
  --jars [JARS]         Provide jars to edit a Notebook.
  --packages [PACKAGES]
                        Provide packages to edit a Notebook.
  --driver-memory [DRIVER_MEMORY]
                        Provide driver-memory to edit a Notebook.
  --executor-memory [EXECUTOR_MEMORY]
                        Provide executor-memory to edit a Notebook.
  --driver-cores [DRIVER_CORES]
                        Provide driver-cores to edit a Notebook.
  --total-executor-cores [TOTAL_EXECUTOR_CORES]
                        Provide total-executor-cores to edit a Notebook.
  --executor-cores [EXECUTOR_CORES]
                        Provide executor-cores to edit a Notebook.
  --num-executors [NUM_EXECUTORS]
                        Provide num-executors to edit a Notebook.
  --should_append_params [should_append_params]
                        Determines whether the job-level Spark configuration should append to or override the cluster-level Spark configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- edit example with the required arguments and other optional arguments passed which is to be updated.

```bash
yeedu notebook edit --workspace_id=1 --notebook_id=2 --name=Notebook_01
```

- Console output

```bash
{
  "notebook_id": "2",
  "notebook_name": "Notebook_01",
  "cluster_id": "1",
  "workspace_id": "1",
  "spark_job_type_lang_id": 3,
  "max_concurrency": "1",
  "notebook_file_id": "1",
  "notebook_cells_auto_save": null,
  "conf": null,
  "packages": null,
  "jars": null,
  "files": null,
  "driver_memory": null,
  "executor_memory": null,
  "driver_cores": null,
  "total_executor_cores": null,
  "executor_cores": null,
  "num_executors": null,
  "should_append_params": false,
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T07:12:00.012Z",
  "from_date": "2024-06-14T07:05:31.507Z",
  "to_date": null
}
```

### enable

```bash
yeedu notebook enable -h
```

```bash
usage:  enable [-h] --workspace_id WORKSPACE_ID
                    [--notebook_id NOTEBOOK_ID]
                    [--notebook_name NOTEBOOK_NAME]
                    [--json-output [{pretty,default}]]
                    [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to enable the Notebook.
  --notebook_id NOTEBOOK_ID
                        Provide Notebook Conf Id to enable the Notebook.
  --notebook_name NOTEBOOK_NAME
                        Provide Notebook Name to enable the Notebook.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- enable example with the required arguments passed.

```bash
yeedu notebook enable --workspace_id=1 --notebook_id=2
```

- Console output

```bash
{
  "notebook_id": "2",
  "notebook_name": "Notebook_01",
  "cluster_id": "1",
  "workspace_id": "1",
  "spark_job_type_lang_id": 3,
  "max_concurrency": "1",
  "notebook_file_id": "1",
  "notebook_cells_auto_save": null,
  "conf": null,
  "packages": null,
  "jars": null,
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T07:13:24.656Z",
  "from_date": "2024-06-14T07:05:31.507Z",
  "to_date": null
}
```

### disable

```bash
yeedu notebook disable -h
```

```bash
usage:  disable [-h] --workspace_id WORKSPACE_ID
                     [--notebook_id NOTEBOOK_ID]
                     [--notebook_name NOTEBOOK_NAME]
                     [--json-output [{pretty,default}]]
                     [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to disable the Notebook.
  --notebook_id NOTEBOOK_ID
                        Provide Notebook Conf Id to disable the Notebook.
  --notebook_name NOTEBOOK_NAME
                        Provide Notebook Name to disable the Notebook.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- disable example with the required arguments passed.

```bash
yeedu notebook disable --workspace_id=1 --notebook_id=2
```

- Console output

```bash
{
  "notebook_id": "2",
  "notebook_name": "Notebook_01",
  "cluster_id": "1",
  "workspace_id": "1",
  "spark_job_type_lang_id": 3,
  "max_concurrency": "1",
  "notebook_file_id": "1",
  "notebook_cells_auto_save": null,
  "conf": null,
  "packages": null,
  "jars": null,
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T07:12:37.380Z",
  "from_date": "2024-06-14T07:05:31.507Z",
  "to_date": "2024-06-14T07:12:37.380Z"
}
```

### export

```bash
yeedu notebook export -h
```

```bash
usage:  export [-h] --workspace_id WORKSPACE_ID [--notebook_id NOTEBOOK_ID]
               [--notebook_name NOTEBOOK_NAME] [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to export a specific Notebook
                        from it.
  --notebook_id NOTEBOOK_ID
                        Provide Notebook Id to export a specific Notebook
                        Configuration.
  --notebook_name NOTEBOOK_NAME
                        Provide Notebook name to export a specific Notebook
                        Configuration.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- export example with the required arguments passed.

```bash
yeedu notebook export --workspace_id=1 --notebook_id=1
```

- Console output

```bash
{
  "jobs": [
    {
      "name": "test_notebook_1",
      "spark_job_type": {
        "job_type": "NOTEBOOK",
        "language": "Python3"
      },
      "cluster_info": {
        "cluster_name": "gcp_cluster",
        "cluster_type": "YEEDU"
      },
      "notebook_cells": {
        "cells": [
          {
            "code": "print(\"hello\")",
            "cell_uuid": "f98e6834-09e2-4c59-84d6-130769c9d182"
          }
        ]
      },
      "conf": [],
      "packages": [],
      "jars": [],
      "files": [],
      "driver_memory": null,
      "executor_memory": null,
      "driver_cores": null,
      "total_executor_cores": null,
      "executor_cores": null,
      "num_executors": null,
      "should_append_params": false
    }
  ]
}
```

### clone

```bash
yeedu notebook clone -h
```

```bash
usage:  clone [-h] --workspace_id WORKSPACE_ID [--notebook_id NOTEBOOK_ID] 
                  [--notebook_name NOTEBOOK_NAME] --new_notebook_name NEW_NOTEBOOK_NAME 
                  [--clone_file_path CLONE_FILE_PATH]
                  [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace_id to clone a Notebook.
  --notebook_id NOTEBOOK_ID
                        Provide Notbeook Conf Id to clone a Notebook.
  --notebook_name NOTEBOOK_NAME
                        Provide Notebook Name to clone a Notebook.
  --new_notebook_name NEW_NOTEBOOK_NAME
                        Provide notebook_name to clone a Notebook.
  --clone_file_path CLONE_FILE_PATH
                        Provide notebook_path to clone a Notebook.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- clone example with the required arguments passed.

```bash
yeedu notebook clone --workspace_id 9 --notebook_id 15 --new_notebook_name="cloned_notebook"
```

- Console output

```bash
{
  "message": "Successfully cloned Notebook Conf Id: 15 to new Notebook Name: 'cloned_notebook'."
}
```

## Notebook Runs

| Command Name                          | Utility                                                 |
| ------------------------------------- | ------------------------------------------------------- |
| [start](#start-2)                     | To start a Notebook run.                                |
| [kernel-start](#kernel-start)         | To start a kernel of a Notebook run.                    |
| [kernel-status](#kernel-status)       | To get the status of the kernel of a Notebook run.      |
| [kernel-interrupt](#kernel-interrupt) | To interrupt a kernel of a Notebook run.                |
| [kernel-restart](#kernel-restart)     | To restart a kernel of a Notebook run.                  |
| [list-runs](#list-runs-1)             | To list all the available Notebook runs.                |
| [search-runs](#search-runs-1)         | To search Notebook runs by similar notebook name.       |
| [get-run](#get-run-1)                 | To get information about a specific Notebook run.       |
| [stop](#stop-2)                       | To stop a specific Notebook run.                        |
| [logs](#logs-2)                       | To download Notebook run logs.                          |

### start

```bash
yeedu notebook start -h
```

```bash
usage:  start [-h] --workspace_id WORKSPACE_ID
              [--notebook_id NOTEBOOK_ID]
              [--notebook_name NOTEBOOK_NAME]
              [--json-output [{pretty,default}]]
              [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        To start a Notebook run, enter workspace_id.
  --notebook_id NOTEBOOK_ID
                        To start a Notebook run, enter notebook_id.
  --notebook_name NOTEBOOK_NAME
                        To start a Notebook run, enter notebook_name.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- start example with one of the required argument passed.

```bash
yeedu notebook start --workspace_id=1 --notebook_id=2
```

- Console output

```bash
{
  "run_id": "6",
  "notebook_id": "2",
  "cluster_id": "1",
  "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T07:14:00.801Z",
  "from_date": "2024-06-14T07:14:00.801Z",
  "to_date": null
}
```

### kernel-start

```bash
yeedu notebook kernel-start -h
```

```bash
usage:  kernel-start [-h] --workspace_id WORKSPACE_ID --run_id RUN_ID
                     [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        To start a kernel of a Notebook run, enter workspace_id.
  --run_id RUN_ID
                        To start a kernel of a Notebook run, enter notebook
                        instance id.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- kernel-start example with all the required arguments passed.

```bash
yeedu notebook kernel-start --workspace_id=1 --run_id=6
```

- Console output

```bash
{
  "run_id": 6,
  "kernel_info": {
    "kernel_id": "bb1e6741-dac6-4bdb-83f6-8e683979248e",
    "kernel_status": "starting"
  }
}
```

### kernel-status

```bash
yeedu notebook kernel-status -h
```

```bash
usage:  kernel-status [-h] --workspace_id WORKSPACE_ID --run_id RUN_ID [--json-output [{pretty,default}]]
                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        To get the status of the kernel, enter workspace_id.
  --run_id RUN_ID
                        To get the status of the kernel for a Notebook run, enter notebook run id.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- kernel-status example with all the required arguments passed.

```bash
yeedu notebook kernel-status --workspace_id=1 --run_id=1
```

- Console output

```bash
{
  "run_id": 1,
  "kernel_info": {
    "kernel_id": "71e6acb5-d4d8-4311-a4a3-7f8a8d6a0291",
    "kernel_status": "idle"
  },
  "session_id": "a708b294-8c6a-4ab0-b14f-dbea19bbf2ac"
}
```

### kernel-interrupt

```bash
yeedu notebook kernel-interrupt -h
```

```bash
usage:  kernel-interrupt [-h] --workspace_id WORKSPACE_ID --run_id RUN_ID
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        To interrupt a kernel of a Notebook run, enter
                        workspace_id.
  --run_id RUN_ID
                        To interrupt a kernel of a Notebook run, enter notebook
                        instance id.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- kernel-interrupt example with required and optional arguments passed.

```bash
yeedu notebook kernel-interrupt --workspace_id=1 --run_id=6
```

- Console output

```bash
{
  "run_id": 6,
  "kernel_info": {
    "kernel_id": "bb1e6741-dac6-4bdb-83f6-8e683979248e",
    "kernel_status": "starting"
  }
}
```

### kernel-restart

```bash
yeedu notebook kernel-restart -h
```

```bash
usage:  kernel-restart [-h] --workspace_id WORKSPACE_ID --run_id RUN_ID
                       [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        To restart a kernel of a Notebook run, enter workspace_id.
  --run_id RUN_ID
                        To restart a kernel of a Notebook run, enter notebook
                        instance id.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- kernel-restart example with all the required arguments passed.

```bash
yeedu notebook kernel-restart --workspace_id=1 --run_id=6
```

- Console output

```bash
{
  "run_id": 6,
  "kernel_info": {
    "kernel_id": "bb1e6741-dac6-4bdb-83f6-8e683979248e",
    "kernel_status": "busy"
  }
}
```

### list-runs

```bash
yeedu notebook list-runs -h
```

```bash
usage:  list-runs [-h] --workspace_id WORKSPACE_ID [--cluster_ids [CLUSTER_IDS]] [--notebook_ids [NOTEBOOK_IDS]] [--run_status [RUN_STATUS]] [--job_type_langs [JOB_TYPE_LANGS]]
             [--created_by_ids [CREATED_BY_IDS]] [--modified_by_ids [MODIFIED_BY_IDS]] [--page_number PAGE_NUMBER] [--limit LIMIT] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        To list Notebook runs of a specific workspace_id.
  --cluster_ids [CLUSTER_IDS]
                        To list Notebook runs for optional set of cluster Ids.
  --notebook_ids [NOTEBOOK_IDS]
                        To list Notebook runs for optional set of Notebook Ids.
  --run_status [RUN_STATUS]
                        To list Notebook runs for optional set of run_status. Choices are: submitted, running, done, error, terminated, stopping, stopped
  --job_type_langs [JOB_TYPE_LANGS]
                        An optional set of language filter for Notebook runs. Choices are: Python3, Scala, SQL
  --created_by_ids [CREATED_BY_IDS]
                        To list Notebook runs for optional set of created by user Ids.
  --modified_by_ids [MODIFIED_BY_IDS]
                        To list Notebook runs for optional set of modified by user Ids.
  --page_number PAGE_NUMBER
                        To list Notebook runs for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of job runs. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list example with all the required and optional arguments passed.

```bash
yeedu notebook list --workspace_id=1 --run_status=running
```

- Console output

```bash
{
  "data": [
    {
      "run_id": 6,
      "notebook_url": "http://yeedu3-87cdc71b-e8ad-cbda-15b3-ec4694e7826a.us-central1-a.c.yeedu.internal:8888",
      "run_status": "RUNNING",
      "notebook_conf": {
        "notebook_id": 2,
        "notebook_name": "Notebook_01",
        "notebook_job_type": {
          "job_type": "NOTEBOOK",
          "language": "Python3"
        },
        "cluster_info": {
          "cluster_id": 1,
          "name": "gcp_test",
          "cluster_status": "RUNNING",
          "cluster_type": "YEEDU",
          "instance_size": 1,
          "min_instances": 1,
          "max_instances": 1,
          "cloud_env": {
            "cloud_env_id": 1,
            "name": "gcp",
            "cloud_provider": {
              "cloud_provider_id": 0,
              "name": "GCP"
            }
          },
          "cluster_conf": {
            "cluster_conf_id": 10,
            "cluster_conf_name": "n1-standard-4",
            "machine_type_category": "general_purpose",
            "machine_type": {
              "machine_type_id": 10,
              "name": "n1-standard-4",
              "vCPUs": 4,
              "memory": "15 GiB",
              "has_cuda": false,
              "gpu_model": null,
              "gpus": 0,
              "gpu_memory": null,
              "cpu_model": [
                "Intel Xeon Scalable (Skylake) 1st Generation",
                "Intel Xeon E5 v4 (Broadwell E5)",
                "Intel Xeon E5 v3 (Haswell)",
                "Intel Xeon E5 v2 (Ivy Bridge)",
                "Intel Xeon E5 (Sandy Bridge)"
              ],
              "cpu_min_frequency_GHz": [
                "2.0",
                "2.2",
                "2.3",
                "2.5",
                "2.6"
              ],
              "cpu_max_frequency_GHz": [
                "3.5",
                "3.7",
                "3.8",
                "3.5",
                "3.6"
              ],
              "has_local_disk": false,
              "local_disk_size_GB": null,
              "local_num_of_disks": null,
              "local_disk_throughput_MB": null,
              "machine_price_ycu": 2.5
            },
            "machine_volume_conf": {
              "volume_conf_id": 2,
              "name": "volume_gcp_2",
              "size": 375,
              "machine_volume_num": 2,
              "machine_volume_strip_num": 2
            }
          },
          "spark_infra_version": {
            "spark_infra_version_id": 1,
            "spark_docker_image_name": "v3.2.2-20",
            "spark_version": "3.2.2",
            "hive_version": "3.2.3",
            "hadoop_version": "3.2.4",
            "scala_version": "2.12.15",
            "python_version": "3.9.5",
            "notebook_support": true,
            "has_cuda_support": true,
            "thrift_support": true,
            "yeedu_functions_support": true
          },
          "engine_cluster_spark_config": {
            "max_parallel_spark_job_execution_per_instance": 5,
            "num_of_workers": null
          }
        }
      },
      "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-06-14T07:14:00.801317+00:00",
      "from_date": "2024-06-14T07:14:00.801317+00:00",
      "to_date": "infinity"
    }
  ]
}
```

### search-runs

```bash
yeedu notebook search-runs -h
```

```bash
usage:  search-runs [-h] --workspace_id WORKSPACE_ID --notebook_name NOTEBOOK_NAME [--cluster_ids [CLUSTER_IDS]] [--notebook_ids [NOTEBOOK_IDS]] [--run_status [RUN_STATUS]]
               [--job_type_langs [JOB_TYPE_LANGS]] [--created_by_ids [CREATED_BY_IDS]] [--modified_by_ids [MODIFIED_BY_IDS]] [--page_number PAGE_NUMBER] [--limit LIMIT] [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to search Notebook runs in it.
  --notebook_name NOTEBOOK_NAME
                        Provide notebook_name to search Notebook runs.
  --cluster_ids [CLUSTER_IDS]
                        To search Notebook runs for optional set of cluster Ids.
  --notebook_ids [NOTEBOOK_IDS]
                        To search Notebook runs for optional set of Notebook Ids.
  --run_status [RUN_STATUS]
                        To search Notebook runs for optional set of run_status. Choices are: submitted, running, done, error, terminated, stopping, stopped
  --job_type_langs [JOB_TYPE_LANGS]
                        An optional set of language filter for Notebook runs. Choices are: Python3, Scala, SQL
  --created_by_ids [CREATED_BY_IDS]
                        To search Notebook runs for optional set of created by user Ids.
  --modified_by_ids [MODIFIED_BY_IDS]
                        To search Notebook runs for optional set of modified by user Ids.
  --page_number PAGE_NUMBER
                        To search Notebook runs for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of Notebook runs. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search example with all the required and optional arguments passed.

```bash
yeedu notebook search --workspace_id=1 --notebook_name="Note" --limit=1
```

- Console output

```bash
{
  "data": [
    {
      "run_id": 6,
      "notebook_url": "http://yeedu3-87cdc71b-e8ad-cbda-15b3-ec4694e7826a.us-central1-a.c.yeedu.internal:8888",
      "run_status": "RUNNING",
      "notebook_conf": {
        "notebook_id": 2,
        "notebook_name": "Notebook_01",
        "notebook_job_type": {
          "job_type": "NOTEBOOK",
          "language": "Python3"
        },
        "cluster_info": {
          "cluster_id": 1,
          "name": "gcp_test",
          "cluster_status": "RUNNING",
          "cluster_type": "YEEDU",
          "instance_size": 1,
          "min_instances": 1,
          "max_instances": 1,
          "cloud_env": {
            "cloud_env_id": 1,
            "name": "gcp",
            "cloud_provider": {
              "cloud_provider_id": 0,
              "name": "GCP"
            }
          },
          "cluster_conf": {
            "cluster_conf_id": 10,
            "cluster_conf_name": "n1-standard-4",
            "machine_type_category": "general_purpose",
            "machine_type": {
              "machine_type_id": 10,
              "name": "n1-standard-4",
              "vCPUs": 4,
              "memory": "15 GiB",
              "has_cuda": false,
              "gpu_model": null,
              "gpus": 0,
              "gpu_memory": null,
              "cpu_model": [
                "Intel Xeon Scalable (Skylake) 1st Generation",
                "Intel Xeon E5 v4 (Broadwell E5)",
                "Intel Xeon E5 v3 (Haswell)",
                "Intel Xeon E5 v2 (Ivy Bridge)",
                "Intel Xeon E5 (Sandy Bridge)"
              ],
              "cpu_min_frequency_GHz": [
                "2.0",
                "2.2",
                "2.3",
                "2.5",
                "2.6"
              ],
              "cpu_max_frequency_GHz": [
                "3.5",
                "3.7",
                "3.8",
                "3.5",
                "3.6"
              ],
              "has_local_disk": false,
              "local_disk_size_GB": null,
              "local_num_of_disks": null,
              "local_disk_throughput_MB": null,
              "machine_price_ycu": 2.5
            },
            "machine_volume_conf": {
              "volume_conf_id": 2,
              "name": "volume_gcp_2",
              "size": 375,
              "machine_volume_num": 2,
              "machine_volume_strip_num": 2
            }
          },
          "spark_infra_version": {
            "spark_infra_version_id": 1,
            "spark_docker_image_name": "v3.2.2-20",
            "spark_version": "3.2.2",
            "hive_version": "3.2.3",
            "hadoop_version": "3.2.4",
            "scala_version": "2.12.15",
            "python_version": "3.9.5",
            "notebook_support": true,
            "has_cuda_support": true,
            "thrift_support": true,
            "yeedu_functions_support": true
          },
          "engine_cluster_spark_config": {
            "max_parallel_spark_job_execution_per_instance": 5,
            "num_of_workers": null
          }
        }
      },
      "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-06-14T07:14:00.801317+00:00",
      "from_date": "2024-06-14T07:14:00.801317+00:00",
      "to_date": "infinity"
    }
  ]
}
```

### get-run

```bash
yeedu notebook get-run -h
```

```bash
usage:  get-run [-h] --workspace_id WORKSPACE_ID --run_id RUN_ID
            [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to get information about a specific
                        Notebook run.
  --run_id RUN_ID
                        Provide notebook run id to get information about a specific
                        Notebook run.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get example with all the required arguments passed.

```bash
yeedu notebook get --workspace_id=1 --run_id=6
```

- Console output

```bash
{
  "run_id": 6,
  "notebook_url": "http://yeedu3-87cdc71b-e8ad-cbda-15b3-ec4694e7826a.us-central1-a.c.yeedu.internal:8888",
  "run_status": "RUNNING",
  "execution_time_sec": 484.339894,
  "total_run_time_sec": 486.846376,
  "notebook_conf": {
    "notebook_id": 2,
    "notebook_name": "Notebook_01",
    "notebook_job_type": {
      "job_type": "NOTEBOOK",
      "language": "Python3"
    },
    "cluster_info": {
      "cluster_id": 1,
      "name": "gcp_test",
      "cluster_status": "RUNNING",
      "cluster_type": "YEEDU",
      "instance_size": 1,
      "min_instances": 1,
      "max_instances": 1,
      "cloud_env": {
        "cloud_env_id": 1,
        "name": "gcp",
        "cloud_provider": {
          "cloud_provider_id": 0,
          "name": "GCP"
        }
      },
      "cluster_conf": {
        "cluster_conf_id": 10,
        "cluster_conf_name": "n1-standard-4",
        "machine_type_category": "general_purpose",
        "machine_type": {
          "machine_type_id": 10,
          "name": "n1-standard-4",
          "vCPUs": 4,
          "memory": "15 GiB",
          "has_cuda": false,
          "gpu_model": null,
          "gpus": 0,
          "gpu_memory": null,
          "cpu_model": [
            "Intel Xeon Scalable (Skylake) 1st Generation",
            "Intel Xeon E5 v4 (Broadwell E5)",
            "Intel Xeon E5 v3 (Haswell)",
            "Intel Xeon E5 v2 (Ivy Bridge)",
            "Intel Xeon E5 (Sandy Bridge)"
          ],
          "cpu_min_frequency_GHz": [
            "2.0",
            "2.2",
            "2.3",
            "2.5",
            "2.6"
          ],
          "cpu_max_frequency_GHz": [
            "3.5",
            "3.7",
            "3.8",
            "3.5",
            "3.6"
          ],
          "has_local_disk": false,
          "local_disk_size_GB": null,
          "local_num_of_disks": null,
          "local_disk_throughput_MB": null,
          "machine_price_ycu": 2.5
        },
        "machine_volume_conf": {
          "volume_conf_id": 2,
          "name": "volume_gcp_2",
          "size": 375,
          "machine_volume_num": 2,
          "machine_volume_strip_num": 2
        }
      },
      "spark_infra_version": {
        "spark_infra_version_id": 1,
        "spark_docker_image_name": "v3.2.2-20",
        "spark_version": "3.2.2",
        "hive_version": "3.2.3",
        "hadoop_version": "3.2.4",
        "scala_version": "2.12.15",
        "python_version": "3.9.5",
        "notebook_support": true,
        "has_cuda_support": true,
        "thrift_support": true,
        "yeedu_functions_support": true
      },
      "engine_cluster_spark_config": {
        "max_parallel_spark_job_execution_per_instance": 5,
        "num_of_workers": null
      }
    }
  },
  "workflow_job_instance_details": {
    "workflow_job_instance_status": {
      "workflow_job_instance_id": 7,
      "workflow_job_id": 7,
      "status": "EXECUTING",
      "from_date": "2024-06-14T07:14:00.801317+00:00",
      "to_date": "infinity"
    },
    "workflow_execution_process": {
      "machine_pid_number": "940",
      "machine_hostname": "yeedu1-bcd2b294-deb1-10c9-0b8e-8e471e5c46f3",
      "machine_id": "bcd2b294-deb1-10c9-0b8e-8e471e5c46f3",
      "machine_pid_user": "root",
      "machine_node_number": "0"
    }
  },
  "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
  "created_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "last_update_date": "2024-06-14T07:14:00.801317+00:00",
  "from_date": "2024-06-14T07:14:00.801317+00:00",
  "to_date": "infinity"
}
```

### stop

```bash
yeedu notebook stop -h
```

```bash
usage:  stop [-h] --workspace_id WORKSPACE_ID --run_id RUN_ID
             [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide workspace id to stop a specific Notebook run.
  --run_id RUN_ID
                        Provide notebook run id to stop a specific Notebook
                        Instance.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- stop example with all the required argument passed.

```bash
yeedu notebook stop --workspace_id=1 --run_id=6
```

- Console output

```bash
{
  "SparkKill": {
    "workflow_job_id": 7,
    "workflow_job_instance_id": 7,
    "spark_job_instance_id": 6,
    "spark_job_id": 2,
    "compute_engine_id": 1
  }
}
```

### logs

```bash
yeedu notebook logs -h
```

```bash
usage:  logs [-h] --workspace_id WORKSPACE_ID --run_id RUN_ID [--log_type {stdout,stderr}] [--last_n_lines LAST_N_LINES] [--file_size_bytes FILE_SIZE_BYTES] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Provide Workspace Id to download Notebook run logs.
  --run_id RUN_ID
                        Provide Notebook Id to download Notebook run logs.
  --log_type {stdout,stderr}
                        Provide log type to download Notebook run logs. (default: stdout)
  --last_n_lines LAST_N_LINES
                        Number of lines to retrieve from the end of the log file (sample preview).
  --file_size_bytes FILE_SIZE_BYTES
                        Number of bytes to preview from the beginning of the log file (sample preview).
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- logs example with all the required arguments passed.

```bash
yeedu notebook logs --workspace_id=1 --run_id=6 --log_type="stderr"
```

- Console output

```bash
[I 2024-06-14 07:28:42.657 ServerApp] jupyter_lsp | extension was successfully linked.
[I 2024-06-14 07:28:42.663 ServerApp] jupyter_server_terminals | extension was successfully linked.
[I 2024-06-14 07:28:42.669 ServerApp] jupyterlab | extension was successfully linked.
[I 2024-06-14 07:28:42.675 ServerApp] notebook | extension was successfully linked.
[I 2024-06-14 07:28:42.974 ServerApp] notebook_shim | extension was successfully linked.
[I 2024-06-14 07:28:43.000 ServerApp] notebook_shim | extension was successfully loaded.
[I 2024-06-14 07:28:43.003 ServerApp] jupyter_lsp | extension was successfully loaded.
[I 2024-06-14 07:28:43.005 ServerApp] jupyter_server_terminals | extension was successfully loaded.
[I 2024-06-14 07:28:43.007 LabApp] JupyterLab extension loaded from /usr/local/lib/python3.9/dist-packages/jupyterlab
[I 2024-06-14 07:28:43.007 LabApp] JupyterLab application directory is /usr/local/share/jupyter/lab
[I 2024-06-14 07:28:43.008 LabApp] Extension Manager is 'pypi'.
[I 2024-06-14 07:28:43.026 ServerApp] jupyterlab | extension was successfully loaded.
[I 2024-06-14 07:28:43.031 ServerApp] notebook | extension was successfully loaded.
[I 2024-06-14 07:28:43.032 ServerApp] Serving notebooks from local directory: /opt/spark
[I 2024-06-14 07:28:43.032 ServerApp] Jupyter Server 2.14.1 is running at:
[I 2024-06-14 07:28:43.032 ServerApp] http://yeedu3-87cdc71b-e8ad-cbda-15b3-ec4694e7826a.us-central1-a.c.yeedu.internal:8888/tree?token=5d2d7e2eeb0c96faf0f8b34dcbf29ca6fcfd643140fe7b38
[I 2024-06-14 07:28:43.032 ServerApp]     http://127.0.0.1:8888/tree?token=5d2d7e2eeb0c96faf0f8b34dcbf29ca6fcfd643140fe7b38
[I 2024-06-14 07:28:43.032 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 2024-06-14 07:28:43.038 ServerApp]

...
...
    To access the server, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/jpserver-1694-open.html
    Or copy and paste one of these URLs:
        http://yeedu3-87cdc71b-e8ad-cbda-15b3-ec4694e7826a.us-central1-a.c.yeedu.internal:8888/tree?token=5d2d7e2eeb0c96faf0f8b34dcbf29ca6fcfd643140fe7b38
        http://127.0.0.1:8888/tree?token=5d2d7e2eeb0c96faf0f8b34dcbf29ca6fcfd643140fe7b38
...

Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
...

```

# Billing

| Command Name                    | Utility                                      |
| ------------------------------- | -------------------------------------------- |
| [tenants](#tenants)             | To retrieve a list of billed tenants.        |
| [date-range](#date-range)       | To retrieve a list of billed date range.     |
| [clusters](#clusters)           | To retrieve a list of billed clusters.       |
| [machine-types](#machine-types) | To retrieve a list of billed machine types.  |
| [labels](#labels)               | To retrieve a list of billed cluster labels. |
| [usage](#usage)                 | To list the billed usage.                    |
| [invoice](#invoice)             | To list the billed invoice.                  |

### tenants

```bash
yeedu billing tenants -h
```

```bash
usage:  tenants [-h] [--billing_type [{usage,invoice}]]
                [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --billing_type [{usage,invoice}]
                        Specifies the billing type to be used as a filter. (default:
                        usage)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- tenants example.

```bash
yeedu billing tenants
```

- Console output

```bash
[
  {
    "tenant_id": "d1061751-19f2-49d0-8072-270144ddf289",
    "tenant_name": "yeedu_dev_gang"
  },
  {
    "tenant_id": "ec234745-4625-4abc-9ae7-1f8a9a9090b3",
    "tenant_name": "demo_tenant"
  }
]
```

### date-range

```bash
yeedu billing date-range -h
```

```bash
usage:  date-range [-h] [--billing_type [{usage,invoice}]] [--tenant_ids [TENANT_IDS]]
                   [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --billing_type [{usage,invoice}]
                        Specifies the billing type to be used as a filter. (default:
                        usage)
  --tenant_ids [TENANT_IDS]
                        Specifies the tenant IDs to be used as a filter.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- date-range example with an optional argument passed.

```bash
yeedu billing date-range --billing_type=usage
```

- Console output

```bash
{
  "dates": [
    "2024-06-26",
    "2024-06-25"
  ]
}
```

### clusters

```bash
yeedu billing clusters -h
```

```bash
usage:  clusters [-h] [--billing_type [{usage,invoice}]] [--tenant_ids [TENANT_IDS]]
                 [--cloud_providers [CLOUD_PROVIDERS]]
                 [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --billing_type [{usage,invoice}]
                        Specifies the billing type to be used as a filter. (default:
                        usage)
  --tenant_ids [TENANT_IDS]
                        Specifies the tenant IDs to be used as a filter.
  --cloud_providers [CLOUD_PROVIDERS]
                        Specifies the cloud providers to be used as a filter. Choices
                        are: GCP, AWS, Azure
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- clusters example with one of the optional argument passed.

```bash
yeedu billing clusters --billing_type=usage
```

- Console output

```bash
[
  {
    "cluster_id": 8,
    "cluster_name": "gcp_cluster",
    "tenant_id": "ec234745-4625-4abc-9ae7-1f8a9a9090b3",
    "tenant_name": "demo_tenant",
    "cloud_provider_id": 0,
    "cloud_provider_name": "GCP"
  },
  {
    "cluster_id": 7,
    "cluster_name": "aws_cluster",
    "tenant_id": "ec234745-4625-4abc-9ae7-1f8a9a9090b3",
    "tenant_name": "demo_tenant",
    "cloud_provider_id": 1,
    "cloud_provider_name": "AWS"
  },
  {
    "cluster_id": 6,
    "cluster_name": "spring",
    "tenant_id": "d1061751-19f2-49d0-8072-270144ddf289",
    "tenant_name": "yeedu_dev_gang",
    "cloud_provider_id": 2,
    "cloud_provider_name": "Azure"
  },
  {
    "cluster_id": 5,
    "cluster_name": "winter",
    "tenant_id": "d1061751-19f2-49d0-8072-270144ddf289",
    "tenant_name": "yeedu_dev_gang",
    "cloud_provider_id": 1,
    "cloud_provider_name": "AWS"
  },
  {
    "cluster_id": 4,
    "cluster_name": "summer",
    "tenant_id": "d1061751-19f2-49d0-8072-270144ddf289",
    "tenant_name": "yeedu_dev_gang",
    "cloud_provider_id": 0,
    "cloud_provider_name": "GCP"
  },
  {
    "cluster_id": 3,
    "cluster_name": "performance_test",
    "tenant_id": "ec234745-4625-4abc-9ae7-1f8a9a9090b3",
    "tenant_name": "demo_tenant",
    "cloud_provider_id": 1,
    "cloud_provider_name": "AWS"
  },
  {
    "cluster_id": 2,
    "cluster_name": "dev_test_cluster",
    "tenant_id": "ec234745-4625-4abc-9ae7-1f8a9a9090b3",
    "tenant_name": "demo_tenant",
    "cloud_provider_id": 1,
    "cloud_provider_name": "AWS"
  },
  {
    "cluster_id": 1,
    "cluster_name": "500k_jobs_load_test_cluster",
    "tenant_id": "ec234745-4625-4abc-9ae7-1f8a9a9090b3",
    "tenant_name": "demo_tenant",
    "cloud_provider_id": 1,
    "cloud_provider_name": "AWS"
  }
]
```

### machine-types

```bash
yeedu billing machine-types -h
```

```bash
usage:  machine-types [-h] [--billing_type [{usage,invoice}]]
                      [--tenant_ids [TENANT_IDS]] [--cloud_providers [CLOUD_PROVIDERS]]
                      [--cluster_ids [CLUSTER_IDS]] [--json-output [{pretty,default}]]
                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --billing_type [{usage,invoice}]
                        Specifies the billing type to be used as a filter. (default:
                        usage)
  --tenant_ids [TENANT_IDS]
                        Specifies the tenant IDs to be used as a filter.
  --cloud_providers [CLOUD_PROVIDERS]
                        Specifies the cloud providers to be used as a filter. Choices
                        are: GCP, AWS, Azure
  --cluster_ids [CLUSTER_IDS]
                        Specifies the cluster instance IDs to be used as a filter.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- machine-types example with one of the optional argument passed.

```bash
yeedu billing machine-types --billing_type=usage
```

- Console output

```bash
[
  {
    "machine_type_id": 87,
    "machine_type_name": "m5d.4xlarge"
  },
  {
    "machine_type_id": 10,
    "machine_type_name": "n1-standard-4"
  },
  {
    "machine_type_id": 86,
    "machine_type_name": "m5d.2xlarge"
  },
  {
    "machine_type_id": 89,
    "machine_type_name": "m5d.xlarge"
  },
  {
    "machine_type_id": 213,
    "machine_type_name": "Standard_D4ads_v5"
  }
]
```

### labels

```bash
yeedu billing labels -h
```

```bash
usage:  labels [-h] [--billing_type [{usage,invoice}]] [--tenant_ids [TENANT_IDS]]
               [--cloud_providers [CLOUD_PROVIDERS]] [--cluster_ids [CLUSTER_IDS]]
               [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --billing_type [{usage,invoice}]
                        Specifies the billing type to be used as a filter. (default:
                        usage)
  --tenant_ids [TENANT_IDS]
                        Specifies the tenant IDs to be used as a filter.
  --cloud_providers [CLOUD_PROVIDERS]
                        Specifies the cloud providers to be used as a filter. Choices
                        are: GCP, AWS, Azure
  --cluster_ids [CLUSTER_IDS]
                        Specifies the cluster instance IDs to be used as a filter.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- labels example with one of the optional argument passed.

```bash
yeedu billing labels --billing_type=usage
```

- Console output

```bash
{
  "created-for": [
    "dev_jobs_test",
    "load-test"
  ],
  "resource": [
    "yeedu"
  ],
  "team": [
    "summer",
    "spring"
  ],
  "tenant_id": [
    "d1061751-19f2-49d0-8072-270144ddf289",
    "ec234745-4625-4abc-9ae7-1f8a9a9090b3"
  ],
  "vm": [
    "yeedu_node"
  ]
}
```

### usage

```bash
yeedu billing usage -h
```

```bash
usage:  usage [-h] [--tenant_ids [TENANT_IDS]] --start_date START_DATE --end_date
              END_DATE [--cloud_providers [CLOUD_PROVIDERS]]
              [--cluster_ids [CLUSTER_IDS]] [--machine_type_ids [MACHINE_TYPE_IDS]]
              [--labels LABELS [LABELS ...]] [--json-output [{pretty,default}]]
              [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_ids [TENANT_IDS]
                        Provide the tenant_ids to list billed usage.
  --start_date START_DATE
                        Provide the start_date of billed date.
  --end_date END_DATE   Provide the end_date of billed date.
  --cloud_providers [CLOUD_PROVIDERS]
                        Provide cloud_providers to list billed usage for given cloud
                        providers. Choices are: GCP, AWS, Azure
  --cluster_ids [CLUSTER_IDS]
                        Provide the cluster_ids to list billed usage.
  --machine_type_ids [MACHINE_TYPE_IDS]
                        Provide the machine_type_ids to list billed usage.
  --labels LABELS [LABELS ...]
                        Provide the labels key-value pair to list billed usage.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- usage example with the optional and required arguments passed.

```bash
yeedu billing usage --start_date="2024-06-26" --end_date="2024-06-27" --labels="team=summer"
```

- Console output

```bash
{
  "usage": [
    {
      "tenant_id": "d1061751-19f2-49d0-8072-270144ddf289",
      "tenant_name": "yeedu_dev_gang",
      "cluster_id": 4,
      "cluster_name": "summer",
      "cluster_labels": {
        "team": "summer",
        "resource": "yeedu",
        "vm": "yeedu_node",
        "tenant_id": "d1061751-19f2-49d0-8072-270144ddf289"
      },
      "cloud_provider_id": 0,
      "cloud_provider_name": "GCP",
      "machine_type_id": 10,
      "machine_type": "n1-standard-4",
      "machine_price_ycu_hour": 2.5,
      "total_daily_minutes": 28,
      "total_daily_ycu": 1.1666666666666667,
      "checkpoint_day": "2024-06-26T00:00:00+00:00",
      "from_date": "2024-06-27T00:24:23.11089+00:00",
      "to_date": "infinity"
    }
  ],
  "usage_overview": {
    "overall_total_minutes": 28,
    "overall_total_ycu": 1.1666666666666667,
    "total_clusters_count": 1,
    "total_tenants": 1
  }
}
```

### invoice

```bash
yeedu billing invoice -h
```

```bash
usage:  invoice [-h] [--tenant_ids [TENANT_IDS]] --start_month_year START_MONTH_YEAR
                --end_month_year END_MONTH_YEAR [--cloud_providers [CLOUD_PROVIDERS]]
                [--cluster_ids [CLUSTER_IDS]] [--machine_type_ids [MACHINE_TYPE_IDS]]
                [--labels LABELS [LABELS ...]] [--json-output [{pretty,default}]]
                [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_ids [TENANT_IDS]
                        Provide the tenant_ids.
  --start_month_year START_MONTH_YEAR
                        Provide the start_month_year of billed date.
  --end_month_year END_MONTH_YEAR
                        Provide the end_month_year of billed date.
  --cloud_providers [CLOUD_PROVIDERS]
                        Provide cloud_providers to list billed invoice for given cloud
                        providers. Choices are: GCP, AWS, Azure
  --cluster_ids [CLUSTER_IDS]
                        Provide the cluster_ids to list billed invoice.
  --machine_type_ids [MACHINE_TYPE_IDS]
                        Provide the machine_type_ids list billed invoice.
  --labels LABELS [LABELS ...]
                        Provide the labels as key-value pair list billed invoice.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- invoice example with the optional and required arguments passed.

```bash
yeedu billing invoice --start_month_year="2024-05-01" --end_month_year="2024-06-01" --labels="team=summer"
```

- Console output

```bash
{
  "invoice": [
    {
      "tenant_id": "d1061751-19f2-49d0-8072-270144ddf289",
      "tenant_name": "yeedu_dev_gang",
      "cluster_id": 4,
      "cluster_name": "summer",
      "cluster_labels": {
        "team": "summer",
        "resource": "yeedu",
        "vm": "yeedu_node",
        "tenant_id": "d1061751-19f2-49d0-8072-270144ddf289"
      },
      "cloud_provider_id": 0,
      "cloud_provider_name": "GCP",
      "machine_type_id": 10,
      "machine_type": "n1-standard-4",
      "machine_price_ycu_hour": 2.5,
      "total_monthly_minutes": 236,
      "total_monthly_ycu": 9.833333333333334,
      "checkpoint_month": "2024-06-01T00:00:00+00:00",
      "from_date": "2024-06-30T00:00:00+00:00",
      "to_date": "infinity"
    }
  ],
  "invoice_overview": {
    "overall_total_minutes": 236,
    "overall_total_ycu": 9.833333333333334,
    "total_clusters_count": 1,
    "total_tenants": 1
  }
}
```

# IAM (Identity and Access Management)

## User

| Command Name                      | Utility                                                       |
| --------------------------------- | ------------------------------------------------------------- |
| [search-tenants](#search-tenants) | Retrieves a list of tenants based on a search by tenant name. |
| [get-user-info](#get-user-info)   | To get information about current session user.                |
| [get-user-roles](#get-user-roles) | To get all the roles of current session user.                 |

### search-tenants

```bash
yeedu iam search-tenants -h
```

```bash
usage:  search-tenants [-h] --tenant_name TENANT_NAME [--page_number PAGE_NUMBER]
                       [--limit LIMIT] [--json-output [{pretty,default}]]
                       [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_name TENANT_NAME
                        Specifies the name of the tenant to search for.
  --page_number PAGE_NUMBER
                        Specifies the page number for the items to return. (default: 1)
  --limit LIMIT         Specifies the numbers of items to return. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```

- search-tenants example with required arguments passed.

```bash
yeedu iam search-tenants --tenant_name="tenant"
```

- Console output

```bash
{
  "data": [
    {
      "tenant_id": "dc16df84-8ded-46be-9cc1-3caf57bded1b",
      "name": "test-tenant",
      "description": "Yeedu Tenant"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-user-info

```bash
yeedu iam get-user-info -h
```

```bash
usage:  get-user-info [-h] [--json-output [{pretty,default}]]
                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-user-info example without any optional arguments passed.

```bash
yeedu iam get-user-info
```

- Console output

```bash
{
  "user_id": "1",
  "tenant_id": null,
  "username": "YSU0000",
  "email": "ysu0000@yeedu.com",
  "group_info": null,
  "from_date": "2024-06-13T11:29:51.951Z",
  "to_date": null
}
```

### get-user-roles

```bash
yeedu iam get-user-roles -h
```

```bash
usage:  get-user-roles [-h] [--tenant_id TENANT_ID]
                       [--json-output [{pretty,default}]]
                       [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide tenant_id to get the user roles in that tenant.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-user-roles example without any optional arguments passed.

```bash
yeedu iam get-user-roles
```

- Console output

```bash
{
  "user_id": 1,
  "username": "YSU0000",
  "email": "ysu0000@yeedu.com",
  "user_roles": [
    {
      "roles_id": 3,
      "user_role": "Platform Admin"
    }
  ],
  "group_roles": null,
  "from_date": "2024-06-13T11:29:51.951785+00:00",
  "to_date": "infinity"
}
```

## Shared Platform and Admin

| Command Name                          | Utility                                             |
| ------------------------------------- | --------------------------------------------------- |
| [sync-user](#sync-user)               | To get the information about a specific User.       |
| [sync-group](#sync-group)             | To get the information about a specific Group.      |
| [list-user-groups](#list-user-groups) | To list all the Groups for a specific User.         |
| [list-users](#list-users-2)           | To list all the available Users.                    |
| [search-users](#search-users-1)       | To search the users based on username.              |
| [match-user](#match-user-1)           | To match exactly the user for the given username.   |
| [list-group-users](#list-group-users) | To list all the Users for a specific Group.         |
| [list-groups](#list-groups-2)         | To list all the available Groups.                   |
| [search-groups](#search-groups)       | To search the groups based on groupname.            |
| [match-group](#match-group-1)         | To match exactly the group for the given groupname. |

### sync-user

```bash
yeedu iam sync-user -h
```

```bash
usage:  sync-user [-h] --username USERNAME
                  [--json-output [{pretty,default}]]
                  [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --username USERNAME   Provide username to get information about a specific User.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- sync-user example with required argument '--username' passed.

```bash
yeedu iam sync-user --username="RU0000"
```

- Console output

```bash
{
  "user_id": "2",
  "username": "RU0000",
  "display_name": "RU0000",
  "email": "ru0000@yeedu.com",
  "from_date": "2024-06-14T07:37:25.892Z",
  "to_date": null
}
```

### sync-group

```bash
yeedu iam sync-group -h
```

```bash
usage:  sync-group [-h] --groupname GROUPNAME
                   [--json-output [{pretty,default}]]
                   [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --groupname GROUPNAME
                        Provide groupname to get information about a specific Group.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- sync-group example with required argument '--groupname' passed.

```bash
yeedu iam sync-group --groupname="yeedu-provider"
```

- Console output

```bash
[
  {
    "group_id": 15,
    "group_name": "yeedu-provider",
    "group_mail": null,
    "group_object_id": null,
    "group_type": null,
    "from_date": "2024-06-14T07:39:05.171932+00:00",
    "to_date": "infinity"
  }
]
```

### list-user-groups

```bash
yeedu iam list-user-groups -h
```

```bash
usage:  list-user-groups [-h] --user_id USER_ID
                         [--page_number PAGE_NUMBER] [--limit LIMIT]
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --user_id USER_ID     Provide user_id to list all the groups for a specific User.
  --page_number PAGE_NUMBER
                        To list groups for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of groups. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-user-groups example with required argument '--user_id' passed.

```bash
yeedu iam list-user-groups --user_id=1
```

- Console output

```bash
{
  "data": [
    {
      "group_id": 4,
      "group_name": "GRP-RU00",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-13T11:29:51.951785+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 3,
      "group_name": "GRP-RP00",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-13T11:29:51.951785+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 2,
      "group_name": "test-yeedu-group",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-13T11:29:51.951785+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 1,
      "group_name": "yeedu-manager",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-13T11:29:51.951785+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 4,
    "total_pages": 1,
    "limit": 100
  }
}
```

### list-users

```bash
yeedu iam list-users -h
```

```bash
usage:  list-users [-h] [--group_id GROUP_ID]
                   [--page_number PAGE_NUMBER] [--limit LIMIT]
                   [--json-output [{pretty,default}]]
                   [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --group_id GROUP_ID   Provide group_id to list all the users for a specific group.
  --page_number PAGE_NUMBER
                        To list users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-users example without any optional arguments passed.

```bash
yeedu iam list-users
```

- Console output

```bash
{
  "data": [
    {
      "user_id": 2,
      "username": "RU0000",
      "display_name": "RU0000",
      "email": "ru0000@yeedu.com"
    },
    {
      "user_id": 1,
      "username": "YSU0000",
      "display_name": "YSU0000",
      "email": "ysu0000@yeedu.com"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 2,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-users

```bash
yeedu iam search-users -h
```

```bash
usage:  search-users [-h] --username USERNAME [--group_id GROUP_ID]
                     [--page_number PAGE_NUMBER] [--limit LIMIT]
                     [--json-output [{pretty,default}]]
                     [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --username USERNAME   Provide username to search users matching username.
  --group_id GROUP_ID   Provide group_id to search all the users of a specific group.
  --page_number PAGE_NUMBER
                        To search users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-users example with the required argument passed.

```bash
yeedu iam search-users --username="Y"
```

- Console output

```bash
{
  "data": [
    {
      "user_id": 1,
      "username": "YSU0000",
      "display_name": "YSU0000",
      "email": "ysu0000@yeedu.com"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### match-user

```bash
yeedu iam match-user -h
```

```bash
usage:  match-user [-h] --username USERNAME
                   [--json-output [{pretty,default}]]
                   [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --username USERNAME   Provide username to get user details.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- match-user example with the required argument passed.

```bash
yeedu iam match-user --username="YSU0000"
```

- Console output

```bash
{
  "user_id": 1,
  "username": "YSU0000",
  "display_name": "YSU0000",
  "email": "ysu0000@yeedu.com",
  "from_date": "2024-06-13T11:29:51.951785+00:00",
  "to_date": "infinity"
}
```

### list-group-users

```bash
yeedu iam list-group-users -h
```

```bash
usage:  list-group-users [-h] --group_id GROUP_ID
                         [--page_number PAGE_NUMBER] [--limit LIMIT]
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --group_id GROUP_ID   Provide group_id to list all the users for a specific Group.
  --page_number PAGE_NUMBER
                        To list users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-group-users example with the required argument '--group_id' passed.

```bash
yeedu iam list-group-users --group_id=2
```

- Console output

```bash
{
  "data": [
    {
      "user_id": 1,
      "username": "YSU0000",
      "display_name": "YSU0000",
      "email": "ysu0000@yeedu.com"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### list-groups

```bash
yeedu iam list-groups -h
```

```bash
usage:  list-groups [-h] [--user_id USER_ID]
                    [--page_number PAGE_NUMBER] [--limit LIMIT]
                    [--json-output [{pretty,default}]]
                    [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --user_id USER_ID     Provide user_id to list all the groups of a specific user.
  --page_number PAGE_NUMBER
                        To list users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-groups example without any optional arguments passed.

```bash
yeedu iam list-groups
```

- Console output

```bash
{
  "data": [
    {
      "group_id": 15,
      "group_name": "yeedu-provider",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-14T07:39:05.171932+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 13,
      "group_name": "yeedu-user",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-14T07:37:25.892197+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 4,
      "group_name": "GRP-RU00",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-13T11:29:51.951785+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 3,
      "group_name": "GRP-RP00",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-13T11:29:51.951785+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 2,
      "group_name": "test-yeedu-group",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-13T11:29:51.951785+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 1,
      "group_name": "yeedu-manager",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-13T11:29:51.951785+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 6,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-groups

```bash
yeedu iam search-groups -h
```

```bash
usage:  search-groups [-h] --groupname GROUPNAME [--user_id USER_ID]
                      [--page_number PAGE_NUMBER] [--limit LIMIT]
                      [--json-output [{pretty,default}]]
                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --groupname GROUPNAME
                        To search all the groups matching provided groupname.
  --user_id USER_ID     Provide user_id to search all the groups of a specific user.
  --page_number PAGE_NUMBER
                        To search groups for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of groups. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-groups example with required argument passed.

```bash
yeedu iam search-groups --groupname="yeedu"
```

- Console output

```bash
{
  "data": [
    {
      "group_id": 15,
      "group_name": "yeedu-provider",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-14T07:39:05.171932+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 13,
      "group_name": "yeedu-user",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-14T07:37:25.892197+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 2,
      "group_name": "test-yeedu-group",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-13T11:29:51.951785+00:00",
      "to_date": "infinity"
    },
    {
      "group_id": 1,
      "group_name": "yeedu-manager",
      "group_type": null,
      "group_mail": null,
      "group_object_id": null,
      "from_date": "2024-06-13T11:29:51.951785+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 4,
    "total_pages": 1,
    "limit": 100
  }
}
```

### match-group

```bash
yeedu iam match-group -h
```

```bash
usage:  match-group [-h] --groupname GROUPNAME
                    [--json-output [{pretty,default}]]
                    [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --groupname GROUPNAME
                        Provide groupname to get information about matching groups.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- match-group example with required argument passed.

```bash
yeedu iam match-group --groupname="yeedu-manager"
```

- Console output

```bash
[
  {
    "group_id": 1,
    "group_name": "yeedu-manager",
    "group_mail": null,
    "group_object_id": null,
    "group_type": null,
    "from_date": "2024-06-13T11:29:51.951785+00:00",
    "to_date": "infinity"
  }
]
```

## Lookup

| Command Name                          | Utility                                                 |
| ------------------------------------- | ------------------------------------------------------- |
| [list-resources](#list-resources)     | To get all the resources.                               |
| [get-resource](#get-resource)         | To get resource details for a specific Resource.        |
| [list-permissions](#list-permissions) | To get all the Permission Types.                        |
| [get-permission](#get-permission)     | To get resource details for a specific Permission Type. |
| [list-roles](#list-roles)             | To get all the Roles.                                   |
| [get-role](#get-role)                 | To get resource details for a specific Role.            |
| [list-rules](#list-rules)             | To get all the Rules.                                   |
| [get-rule](#get-rule)                 | To get resource details for a specific Rule.            |

### list-resources

```bash
yeedu iam list-resources -h
```

```bash
usage:  list-resources [-h] [--json-output [{pretty,default}]]
                       [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-resources example without optional argument passed for the output format.

```bash
yeedu iam list-resources
```

- Console output

```bash
[
  {
    "resource_id": 0,
    "resource_path": "/api/v1/lookup_cloud_providers",
    "from_date": "2023-09-29T15:47:59.340Z",
    "to_date": null
  },
  {
    "resource_id": 1,
    "resource_path": "/api/v1/lookup_cloud_providers/:cloud_provider_id",
    "from_date": "2023-09-29T15:47:59.340Z",
    "to_date": null
  },
  ...
  {
    "resource_id": 194,
    "resource_path": "/api/v1/workspace/stats",
    "from_date": "2024-06-13T10:40:53.269Z",
    "to_date": null
  }
]
```

### get-resource

```bash
yeedu iam get-resource -h
```

```bash
usage:  get-resource [-h] --resource_id RESOURCE_ID [--json-output [{pretty,default}]]
                     [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --resource_id RESOURCE_ID
                        Provide the resource_id to get information about a specific
                        Resource.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-resource example with required argument '--resource_id' passed.

```bash
yeedu iam get-resource --resource_id=18
```

- Console output

```bash
{
  "resource_id": 18,
  "resource_path": "/api/v1/machine/networks",
  "from_date": "2024-06-13T10:40:53.269Z",
  "to_date": null
}
```

### list-permissions

```bash
yeedu iam list-permissions -h
```

```bash
usage:  list-permissions [-h] [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-permissions example without optional argument passed for the output format.

```bash
yeedu iam list-permissions
```

- Console output

```bash
[
  {
    "permission_id": 0,
    "permission": "GET",
    "description": "To list a resource",
    "from_date": "2024-06-13T10:40:53.267Z",
    "to_date": null
  },
  {
    "permission_id": 1,
    "permission": "POST",
    "description": "To create a resource",
    "from_date": "2024-06-13T10:40:53.267Z",
    "to_date": null
  },
  {
    "permission_id": 2,
    "permission": "PUT",
    "description": "To update a resource",
    "from_date": "2024-06-13T10:40:53.267Z",
    "to_date": null
  },
  {
    "permission_id": 3,
    "permission": "DELETE",
    "description": "To delete a resource",
    "from_date": "2024-06-13T10:40:53.267Z",
    "to_date": null
  }
]
```

### get-permission

```bash
yeedu iam get-permission -h
```

```bash
usage:  get-permission [-h] --permission_id PERMISSION_ID
                       [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --permission_id PERMISSION_ID
                        Provide the permission_id to get information about a specific
                        Permission Type.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-permission example with required argument '--permission_id' passed.

```bash
yeedu iam get-permission --permission_id=1
```

- Console output

```bash
{
  "permission_id": 1,
  "permission": "POST",
  "description": "To create a resource",
  "from_date": "2024-06-13T10:40:53.267Z",
  "to_date": null
}
```

### list-roles

```bash
yeedu iam list-roles -h
```

```bash
usage:  list-roles [-h] [--json-output [{pretty,default}]]
                   [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-roles example without any optional arguments passed.

```bash
yeedu iam list-roles
```

- Console output

```bash
[
  {
    "role_id": 4,
    "role": "Platform Billing",
    "description": "Can access all the billing APIs",
    "from_date": "2024-06-13T10:40:53.271Z",
    "to_date": null
  },
  {
    "role_id": 3,
    "role": "Platform Admin",
    "description": "Can access and add or remove tenants across all tenants",
    "from_date": "2024-06-13T10:40:53.271Z",
    "to_date": null
  },
  {
    "role_id": 2,
    "role": "Admin",
    "description": "Can add and remove user and group roles and perform all actions within a tenant.",
    "from_date": "2024-06-13T10:40:53.271Z",
    "to_date": null
  },
  {
    "role_id": 1,
    "role": "Can Manage Cluster",
    "description": "GET (Lookup, Volume Config, Network Config, Boot Disk Image Config, Credentials Config, Object Storage Manager, Object Storage Manager Files, Hive Metastore Config, Cluster Configuration, Cluster Instance, Cluster Access Control, Workspace, Workspace Access Control, Spark Job, Spark Job run, Notebook, Notebook run, User) PUT (Cluster Instance, Spark Job, Workspace, Notebook) POST (Object Storage Manager Files, Cluster Instance, Cluster Access Control, Workspace, Workspace Access Control, Spark Job, Spark Job run, Notebook, Notebook run) DELETE (Object Storage Manager Files, Cluster Access Control, Workspace Access Control)",
    "from_date": "2024-06-13T10:40:53.271Z",
    "to_date": null
  },
  {
    "role_id": 0,
    "role": "User",
    "description": "GET (Lookup, Volume Config, Network Config, Boot Disk Image Config, Credentials Config, Object Storage Manager, Object Storage Manager Files, Hive Metastore Config, Cluster Configuration, Cluster Instance, Cluster Access Control, Workspace, Workspace Access Control, Spark Job, Spark Job run, Notebook, Notebook run, User) PUT (Spark Job, Workspace, Notebook) POST (Object Storage Manager Files, Workspace, Workspace Access Control, Spark Job, Spark Job run, Notebook, Notebook run) DELETE (Workspace Access Control)",
    "from_date": "2024-06-13T10:40:53.271Z",
    "to_date": null
  }
]
```

### get-role

```bash
yeedu iam get-role -h
```

```bash
usage:  get-role [-h] --role_id ROLE_ID [--json-output [{pretty,default}]]
                 [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --role_id ROLE_ID     Provide the role_id to get information about a specific Role.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-role example with required argument '--role_id' passed.

```bash
yeedu iam get-role --role_id=1
```

- Console output

```bash
{
  "role_id": 1,
  "role": "Can Manage Cluster",
  "description": "GET (Lookup, Volume Config, Network Config, Boot Disk Image Config, Credentials Config, Object Storage Manager, Object Storage Manager Files, Hive Metastore Config, Cluster Configuration, Cluster Instance, Cluster Access Control, Workspace, Workspace Access Control, Spark Job, Spark Job run, Notebook, Notebook run, User) PUT (Cluster Instance, Spark Job, Workspace, Notebook) POST (Object Storage Manager Files, Cluster Instance, Cluster Access Control, Workspace, Workspace Access Control, Spark Job, Spark Job run, Notebook, Notebook run) DELETE (Object Storage Manager Files, Cluster Access Control, Workspace Access Control)",
  "from_date": "2024-06-13T10:40:53.271Z",
  "to_date": null
}
```

### list-rules

```bash
yeedu iam list-rules -h
```

```bash
usage:  list-rules [-h] [--json-output [{pretty,default}]]
                   [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-rules example without any optional arguments passed.

```bash
yeedu iam list-rules
```

- Console output

```bash
[
  {
    "rule_id": "1",
    "permission_type": {
      "permission_id": 0,
      "permission": "GET",
      "description": "To list a resource"
    },
    "resource": {
      "resource_id": 1,
      "resource_path": "/api/v1/lookup_cloud_providers/:cloud_provider_id"
    },
    "role": {
      "role_id": 0,
      "role": "User",
      "description": "GET (Lookup, Volume Config, Network Config, Boot Disk Image Config, Credentials Config, Object Storage Manager, Object Storage Manager Files, Hive Metastore Config, Cluster Configuration, Cluster Instance, Cluster Access Control, Workspace, Workspace Access Control, Spark Job, Spark Job run, Notebook, Notebook run, User) PUT (Spark Job, Workspace, Notebook) POST (Object Storage Manager Files, Workspace, Workspace Access Control, Spark Job, Spark Job run, Notebook, Notebook run) DELETE (Workspace Access Control)"
    },
    "from_date": "2024-06-13T10:40:53.272Z",
    "to_date": null
},
  ...
  {
    "rule_id": "754",
    "permission_type": {
      "permission_id": 0,
      "permission": "GET",
      "description": "To list a resource"
    },
    "resource": {
      "resource_id": 194,
      "resource_path": "/api/v1/workspace/stats"
    },
    "role": {
      "role_id": 3,
      "role": "Platform Admin",
      "description": "Can access and add or remove tenants across all tenants"
    },
    "from_date": "2024-06-13T10:40:53.272Z",
    "to_date": null
  }
]
```

### get-rule

```bash
yeedu iam get-rule -h
```

```bash
usage:  get-rule [-h] --rule_id RULE_ID [--json-output [{pretty,default}]]
                 [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --rule_id RULE_ID     Provide the rule_id to get information about a specific Rule.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-rule example with required argument '--rule_id' passed.

```bash
yeedu iam get-rule --rule_id=108
```

- Console output

```bash
{
  "rule_id": "108",
  "permission_type": {
    "permission_id": 0,
    "permission": "GET",
    "description": "To list a resource"
  },
  "resource": {
    "resource_id": 39,
    "resource_path": "/api/v1/cluster/stats"
  },
  "role": {
    "role_id": 1,
    "role": "Can Manage Cluster",
    "description": "GET (Lookup, Volume Config, Network Config, Boot Disk Image Config, Credentials Config, Object Storage Manager, Object Storage Manager Files, Hive Metastore Config, Cluster Configuration, Cluster Instance, Cluster Access Control, Workspace, Workspace Access Control, Spark Job, Spark Job run, Notebook, Notebook run, User) PUT (Cluster Instance, Spark Job, Workspace, Notebook) POST (Object Storage Manager Files, Cluster Instance, Cluster Access Control, Workspace, Workspace Access Control, Spark Job, Spark Job run, Notebook, Notebook run) DELETE (Object Storage Manager Files, Cluster Access Control, Workspace Access Control)"
  },
  "from_date": "2024-06-13T10:40:53.272Z",
  "to_date": null
}
```

### list-workspace-permissions

```bash
yeedu iam list-workspace-permissions -h
```

```bash
usage:  list-workspace-permissions [-h] [--json-output [{pretty,default}]]
                                   [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-workspace-permissions example.

```bash
yeedu iam list-workspace-permissions
```

- Console output

```bash
[
  {
    "permission_id": 3,
    "name": "MANAGE",
    "description": "To list jobs, run jobs, edit Spark jobs, and manage workspace access by adding or removing permissions",
    "from_date": "2024-06-13T10:40:53.392Z",
    "to_date": null
  },
  {
    "permission_id": 2,
    "name": "EDIT",
    "description": "To list, run and edit a spark job in a workspace",
    "from_date": "2024-06-13T10:40:53.392Z",
    "to_date": null
  },
  {
    "permission_id": 1,
    "name": "RUN",
    "description": "To list and run the jobs within a workspace",
    "from_date": "2024-06-13T10:40:53.392Z",
    "to_date": null
  },
  {
    "permission_id": 0,
    "name": "VIEW",
    "description": "To list the jobs inside the workspace",
    "from_date": "2024-06-13T10:40:53.392Z",
    "to_date": null
  }
]
```

### get-workspace-permission

```bash
yeedu iam get-workspace-permission -h
```

```bash
usage:  get-workspace-permission [-h] --permission_id PERMISSION_ID
                                 [--json-output [{pretty,default}]]
                                 [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --permission_id PERMISSION_ID
                        Provide the permission_id to get information about a specific
                        Workspace Access Control Permission.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-workspace-permission example with required argument '--permission_id' passed.

```bash
yeedu iam get-workspace-permission --permission_id=1
```

- Console output

```bash
{
  "permission_id": 1,
  "name": "RUN",
  "description": "To list and run the jobs within a workspace",
  "from_date": "2024-06-13T10:40:53.392Z",
  "to_date": null
}
```

# Platform-Admin

## Tenant

| Command Name                        | Utility                                     |
| ----------------------------------- | ------------------------------------------- |
| [create-tenant](#create-tenant)     | To create a Tenant.                         |
| [list-tenants](#list-tenants-1)     | To list all the available Tenants.          |
| [search-tenants](#search-tenants-1) | To search the tenants with the given name.  |
| [get-tenant](#get-tenant)           | To get information about a specific Tenant. |
| [edit-tenant](#edit-tenant)         | To edit a specific Tenant.                  |
| [delete-tenant](#delete-tenant)     | To delete a specific Tenant.                |

### create-tenant

```bash
yeedu platform-admin create-tenant -h
```

```bash
usage:  create-tenant [-h] --name NAME [--description DESCRIPTION]
                      [--json-output [{pretty,default}]]
                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name NAME           Provide name to create-tenant.
  --description DESCRIPTION
                        Provide description to create-tenant.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-tenant example with all the required and optional arguments passed.

```bash
yeedu platform-admin create-tenant --name="tenant_01" --description="Yeedu Tenant-1"
```

- Console output

```bash
{
  "tenant_id": "414e44d2-6f0f-4edc-a298-427a8a7e6a17",
  "name": "tenant_01",
  "description": "Yeedu Tenant-1",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T08:10:39.163Z",
  "from_date": "2024-06-14T08:10:39.163Z",
  "to_date": null
}
```

### list-tenants

```bash
yeedu platform-admin list-tenants -h
```

```bash
usage:  list-tenants [-h] [--page_number PAGE_NUMBER] [--limit LIMIT]
                     [--json-output [{pretty,default}]]
                     [--yaml-output [{true,false}]]
options:
  -h, --help            show this help message and exit
  --page_number PAGE_NUMBER
                        To list tenants for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of tenants. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-tenants example without any optional arguments passed.

```bash
yeedu platform-admin list-tenants
```

- Console output

```bash
{
  "data": [
    {
      "tenant_id": "414e44d2-6f0f-4edc-a298-427a8a7e6a17",
      "name": "tenant_01",
      "description": "Yeedu Tenant-1",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-06-14T08:10:39.163282+00:00",
      "from_date": "2024-06-14T08:10:39.163282+00:00",
      "to_date": "infinity"
    },
    {
      "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
      "name": "test",
      "description": null,
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-06-13T11:30:03.255245+00:00",
      "from_date": "2024-06-13T11:30:03.255245+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 2,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-tenants

```bash
yeedu platform-admin search-tenants -h
```

```bash
usage:  search-tenants [-h] --tenant_name TENANT_NAME
                       [--page_number PAGE_NUMBER] [--limit LIMIT]
                       [--json-output [{pretty,default}]]
                       [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_name TENANT_NAME
                        Provide the tenant name to get all the matching tenants.
  --page_number PAGE_NUMBER
                        To search tenants on a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of tenants. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-tenants example with required arguments passed.

```bash
yeedu platform-admin search-tenants --tenant_name="tenant"
```

- Console output

```bash
{
  "data": [
    {
      "tenant_id": "414e44d2-6f0f-4edc-a298-427a8a7e6a17",
      "name": "tenant_01",
      "description": "Yeedu Tenant-1",
      "created_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "modified_by": {
        "user_id": 1,
        "username": "YSU0000"
      },
      "last_update_date": "2024-06-14T08:10:39.163282+00:00",
      "from_date": "2024-06-14T08:10:39.163282+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-tenant

```bash
yeedu platform-admin get-tenant -h
```

```bash
usage:  get-tenant [-h] [--tenant_id TENANT_ID]
                   [--tenant_name TENANT_NAME]
                   [--json-output [{pretty,default}]]
                   [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide the tenant_id to get information about a specific Tenant.
  --tenant_name TENANT_NAME
                        Provide the tenant_name to get information about a specific Tenant.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-tenant example with any one of the required argument passed.

```bash
yeedu platform-admin get-tenant --tenant_name="tenant_01"
```

- Console output

```bash
{
  "tenant_id": "414e44d2-6f0f-4edc-a298-427a8a7e6a17",
  "name": "tenant_01",
  "description": "Yeedu Tenant-1",
  "created_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "modified_by": {
    "user_id": 1,
    "username": "YSU0000"
  },
  "last_update_date": "2024-06-14T08:10:39.163282+00:00",
  "from_date": "2024-06-14T08:10:39.163282+00:00",
  "to_date": "infinity"
}
```

### edit-tenant

```bash
yeedu platform-admin edit-tenant -h
```

```bash
usage:  edit-tenant [-h] [--tenant_id TENANT_ID]
                    [--tenant_name TENANT_NAME] [--name [NAME]]
                    [--description [DESCRIPTION]]
                    [--json-output [{pretty,default}]]
                    [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide a specific tenant Id to edit-tenant.
  --tenant_name TENANT_NAME
                        Provide a specific tenant Name to edit-tenant.
  --name [NAME]         Provide name to edit-tenant.
  --description [DESCRIPTION]
                        Provide description to edit-tenant.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- edit-tenant example with any one of the required arguments and other optional argument is passed which is to be updated.

```bash
yeedu platform-admin edit-tenant --tenant_id="414e44d2-6f0f-4edc-a298-427a8a7e6a17" --description="Yeedu Tenant 1"
```

- Console output

```bash
{
  "tenant_id": "414e44d2-6f0f-4edc-a298-427a8a7e6a17",
  "name": "tenant_01",
  "description": "Yeedu Tenant 1",
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T08:12:38.020Z",
  "from_date": "2024-06-14T08:10:39.163Z",
  "to_date": null
}
```

### delete-tenant

```bash
yeedu platform-admin delete-tenant -h
```

```bash
usage:  delete-tenant [-h] [--tenant_id TENANT_ID]
                      [--tenant_name TENANT_NAME]
                      [--json-output [{pretty,default}]]
                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide the tenant_id to delete a specific Tenant.
  --tenant_name TENANT_NAME
                        Provide the tenant_name to delete a specific Tenant.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- delete-tenant example with any one of the required argument passed.

```bash
yeedu platform-admin delete-tenant --tenant_id="414e44d2-6f0f-4edc-a298-427a8a7e6a17"
```

- Console output

```bash
{
  "message": "Deleted tenant id: 414e44d2-6f0f-4edc-a298-427a8a7e6a17."
}
```

## User

| Command Name                                | Utility                                                       |
| ------------------------------------------- | ------------------------------------------------------------- |
| [list-user-tenants](#list-user-tenants)     | To list all the tenants associated to an user.                |
| [list-tenant-users](#list-tenant-users)     | To list all the users present in a tenant.                    |
| [search-tenant-users](#search-tenant-users) | To search all the users present in a tenant.                  |
| [get-tenant-user](#get-tenant-user)         | To get information about a User present in a specific tenant. |
| [get-user-roles](#get-user-roles-1)         | To get all the roles of an User present in a specific tenant. |
| [list-users-roles](#list-users-roles)       | To list all the Users Roles in a specific tenant.             |
| [get-role-users](#get-role-users)           | To get all the users of a Role present in a specific tenant.  |
| [create-user-role](#create-user-role)       | To create an User Role for a specific tenant.                 |
| [delete-user-role](#delete-user-role)       | To delete an User Role of a specific tenant.                  |

### list-user-tenants

```bash
yeedu platform-admin list-user-tenants -h
```

```bash
usage:  list-user-tenants [-h] --user_id USER_ID
                          [--page_number PAGE_NUMBER] [--limit LIMIT]
                          [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --user_id USER_ID     Provide User Id to list all the tenants.
  --page_number PAGE_NUMBER
                        To list tenants for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of tenants. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-user-tenants example with the required argument passed.

```bash
yeedu platform-admin list-user-tenants --user_id=1
```

- Console output

```bash
{
  "data": [
    {
      "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
      "name": "test",
      "description": null
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### list-tenant-users

```bash
yeedu platform-admin list-tenant-users -h
```

```bash
usage:  list-tenant-users [-h] --tenant_id TENANT_ID
                          [--page_number PAGE_NUMBER] [--limit LIMIT]
                          [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to list all the users present in it.
  --page_number PAGE_NUMBER
                        To list tenant users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of tenant users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-tenant-users example with required arguments passed.

```bash
yeedu platform-admin list-tenant-users --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870"
```

- Console output

```bash
{
  "data": [
    {
      "user_id": 1,
      "username": "YSU0000",
      "display_name": "YSU0000",
      "email": "ysu0000@yeedu.com"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-tenant-users

```bash
yeedu platform-admin search-tenant-users -h
```

```bash
usage:  search-tenant-users [-h] --username USERNAME --tenant_id TENANT_ID
                            [--page_number PAGE_NUMBER] [--limit LIMIT]
                            [--json-output [{pretty,default}]]
                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --username USERNAME   Provide username to search all the matching users present in it.
  --tenant_id TENANT_ID
                        Provide Tenant Id to search all the users present in it.
  --page_number PAGE_NUMBER
                        To search tenant users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of tenant users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-tenant-users example with required arguments passed.

```bash
yeedu platform-admin search-tenant-users --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --username="YS"
```

- Console output

```bash
{
  "data": [
    {
      "user_id": 1,
      "username": "YSU0000",
      "user_roles": [
        "Platform Admin"
      ],
      "group_roles": [
        null
      ]
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-tenant-user

```bash
yeedu platform-admin get-tenant-user -h
```

```bash
usage:  get-tenant-user [-h] --tenant_id TENANT_ID --user_id USER_ID
                        [--json-output [{pretty,default}]]
                        [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to get information about a specific User.
  --user_id USER_ID     Provide User Id to get information about a specific User.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-tenant-user example with all the required arguments passed.

```bash
yeedu platform-admin get-tenant-user --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --user_id=1
```

- Console output

```bash
{
  "user_id": 1,
  "username": "YSU0000",
  "display_name": "YSU0000",
  "email": "ysu0000@yeedu.com",
  "from_date": "2024-06-13T11:29:51.951785+00:00",
  "to_date": "infinity"
}
```

### get-user-roles

```bash
yeedu platform-admin get-user-roles -h
```

```bash
usage:  get-user-roles [-h] --tenant_id TENANT_ID --user_id USER_ID
                       [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to get roles of a specific User.
  --user_id USER_ID     Provide User Id to get roles of a specific User.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-user-roles example with the required arguments '--tenant_id' and '--user_id' passed.

```bash
yeedu platform-admin get-user-roles --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --user_id=1
```

- Console output

```bash
{
  "user_id": 1,
  "username": "YSU0000",
  "email": "ysu0000@yeedu.com",
  "user_roles": [
    {
      "role_id": 3,
      "user_role": "Platform Admin"
    }
  ],
  "group_roles": null,
  "from_date": "2024-06-13T11:29:51.951785+00:00",
  "to_date": "infinity"
}
```

### list-users-roles

```bash
yeedu platform-admin list-users-roles -h
```

```bash
usage:  list-users-roles [-h] --tenant_id TENANT_ID
                         [--page_number PAGE_NUMBER] [--limit LIMIT]
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to list User roles.
  --page_number PAGE_NUMBER
                        To list users roles for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of users roles. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-users-roles example with the required argument '--tenant_id' passed.

```bash
yeedu platform-admin list-users-roles --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870"
```

- Console output

```bash
{
  "data": [
    {
      "user_id": 1,
      "username": "YSU0000",
      "user_roles": [
        "Platform Admin"
      ],
      "group_roles": [
        null
      ]
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-role-users

```bash
yeedu platform-admin get-role-users -h
```

```bash
usage:  get-role-users [-h] --tenant_id TENANT_ID --role_id ROLE_ID
                       [--page_number PAGE_NUMBER] [--limit LIMIT]
                       [--json-output [{pretty,default}]]
                       [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to get users in a specific Role.
  --role_id ROLE_ID     Provide Role Id to get users in a specific Role.
  --page_number PAGE_NUMBER
                        To list users for a specific page_number. (default: 1)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-role-users example with the required '--tenant_id' arguments passed.

```bash
yeedu platform-admin get-role-users --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --role_id=3
```

- Console output

```bash
{
  "data": {
    "role_id": 3,
    "users": [
      {
        "user_id": 1,
        "username": "YSU0000",
        "display_name": "YSU0000",
        "email": "ysu0000@yeedu.com"
      }
    ]
  },
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### create-user-role

```bash
yeedu platform-admin create-user-role -h
```

```bash
usage:  create-user-role [-h] [--tenant_id TENANT_ID] --user_id
                         USER_ID --role_id ROLE_ID
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to create-user-role.
  --user_id USER_ID     Provide User Id to create-user-role.
  --role_id ROLE_ID     Provide Role Id to create-user-role.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-user-role example with all the required and optional arguments passed.

```bash
yeedu platform-admin create-user-role --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --user_id=2 --role_id=1
```

- Console output

```bash
{
  "user_roles_id": "2",
  "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
  "user_id": "2",
  "role_id": 1,
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T08:18:18.541Z",
  "from_date": "2024-06-14T08:18:18.541Z",
  "to_date": null
}
```

### delete-user-role

```bash
yeedu platform-admin delete-user-role -h
```

```bash
usage:  delete-user-role [-h] [--tenant_id TENANT_ID] --user_id USER_ID --role_id ROLE_ID
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to delete-user-role.
  --user_id USER_ID     Provide User Id to delete-user-role.
  --role_id ROLE_ID     Provide Role Id to delete-user-role.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- delete-user-role example with the required '--tenant_id' argument passed.

```bash
yeedu platform-admin delete-user-role --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --user_id=2 --role_id=1
```

- Console output

```bash
{
  "message": "Deleted User Roles for the provided tenant_id: '8ad4bd62-839f-4aa7-ba1e-c3112cbbf870', user_id: 2 and role_id: 1."
}
```

## Group

| Command Name                                  | Utility                                                                    |
| --------------------------------------------- | -------------------------------------------------------------------------- |
| [list-tenant-groups](#list-tenant-groups)     | To list all the groups present in a tenant.                                |
| [search-tenant-groups](#search-tenant-groups) | To search all the groups present in a tenant.                              |
| [get-tenant-group](#get-tenant-group)         | To get information about a Group present in a specific tenant.             |
| [get-group-roles](#get-group-roles)           | To get all the roles of a Group present in a specific tenant.              |
| [list-groups-roles](#list-groups-roles)       | To list all the Groups Roles in a specific tenant.                         |
| [get-role-groups](#get-role-groups)           | To get all the groups having a specific Role present in a specific tenant. |
| [create-group-role](#create-group-role)       | To create a Group Role for a specific tenant.                              |
| [delete-group-role](#delete-group-role)       | To delete a Group Role of a specific tenant.                               |

### list-tenant-groups

```bash
yeedu platform-admin list-tenant-groups -h
```

```bash
usage:  list-tenant-groups [-h] --tenant_id TENANT_ID
                           [--page_number PAGE_NUMBER] [--limit LIMIT]
                           [--json-output [{pretty,default}]]
                           [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to list all the groups present in it.
  --page_number PAGE_NUMBER
                        To list tenant groups for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of tenant groups. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-tenant-groups example with required and optional arguments passed.

```bash
yeedu platform-admin list-tenant-groups --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870"
```

- Console output

```bash
{
  "data": [
    {
      "group_id": 15,
      "group_name": "yeedu-provider",
      "group_mail": null,
      "group_object_id": null,
      "group_type": null
    },
    {
      "group_id": 1,
      "group_name": "yeedu-manager",
      "group_mail": null,
      "group_object_id": null,
      "group_type": null
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 2,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-tenant-groups

```bash
yeedu platform-admin search-tenant-groups -h
```

```bash
usage:  search-tenant-groups [-h] --groupname GROUPNAME --tenant_id TENANT_ID
                             [--page_number PAGE_NUMBER] [--limit LIMIT]
                             [--json-output [{pretty,default}]]
                             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --groupname GROUPNAME
                        Provide groupname to search all the matching groups present in
                        it.
  --tenant_id TENANT_ID
                        Provide Tenant Id to search all the groups present in it.
  --page_number PAGE_NUMBER
                        To search tenant groups for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of tenant groups. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-tenant-groups example with required and optional arguments passed.

```bash
yeedu platform-admin search-tenant-groups --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --groupname="yeed"
```

- Console output

```bash
{
  "data": [
    {
      "group_id": 1,
      "group_name": "yeedu-manager",
      "group_mail": null,
      "group_type": null,
      "group_object_id": null,
      "roles": [
        "User"
      ]
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-tenant-group

```bash
yeedu platform-admin get-tenant-group -h
```

```bash
usage:  get-tenant-group [-h] --tenant_id TENANT_ID --group_id GROUP_ID
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID Provide Tenant Id to get information about a specific Group.
  --group_id GROUP_ID   Provide Group Id to get information about a specific Group.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-tenant-group example with required arguments passed.

```bash
yeedu platform-admin get-tenant-group --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --group_id=1
```

- Console output

```bash
{
  "group_id": 1,
  "group_name": "yeedu-manager",
  "group_object_id": null,
  "group_type": null,
  "from_date": "2024-06-13T11:29:51.951785+00:00",
  "to_date": "infinity"
}
```

### get-group-roles

```bash
yeedu platform-admin get-group-roles -h
```

```bash
usage:  get-group-roles [-h] --tenant_id TENANT_ID --group_id GROUP_ID
                        [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to get roles of a specific Group.
  --group_id GROUP_ID   Provide Group Id to get roles of a specific Group.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-group-roles example with the required '--tenant_id' and '--group_id' arguments passed.

```bash
yeedu platform-admin get-group-roles --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --group_id=1
```

- Console output

```bash
{
  "group_id": 1,
  "group_name": "yeedu-manager",
  "group_type": null,
  "roles": [
    "User"
  ]
}
```

### list-groups-roles

```bash
yeedu platform-admin list-groups-roles -h
```

```bash
usage:  list-groups-roles [-h] --tenant_id TENANT_ID
                          [--page_number PAGE_NUMBER] [--limit LIMIT]
                          [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to list Group roles.
  --page_number PAGE_NUMBER
                        To list groups roles for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of groups roles. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-groups-roles example with the required arguments '--tenant_id' passed.

```bash
yeedu platform-admin list-groups-roles --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --limit=1
```

- Console output

```bash
{
  "data": [
    {
      "group_id": 1,
      "group_name": "yeedu-manager",
      "group_mail": null,
      "group_type": null,
      "group_object_id": null,
      "roles": [
        "User"
      ]
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 1
  }
}
```

### get-role-groups

```bash
yeedu platform-admin get-role-groups -h
```

```bash
usage:  get-role-groups [-h] --tenant_id TENANT_ID --role_id ROLE_ID
                        [--page_number PAGE_NUMBER] [--limit LIMIT]
                        [--json-output [{pretty,default}]]
                        [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to get groups in a specific Role.
  --role_id ROLE_ID     Provide Role Id to get groups in a specific Role.
  --page_number PAGE_NUMBER
                        To list groups for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of groups. (default: 100)

  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-role-groups example with the required arguments '--tenant_id' and '--role_id' passed.

```bash
yeedu platform-admin get-role-groups --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --role_id=0
```

- Console output

```bash
{
  "data": {
    "role_id": 0,
    "groups": [
      {
        "group_id": 1,
        "group_name": "yeedu-manager",
        "group_mail": null,
        "group_object_id": null,
        "group_type": null
      },
      {
        "group_id": 15,
        "group_name": "yeedu-provider",
        "group_mail": null,
        "group_object_id": null,
        "group_type": null
      }
    ]
  },
  "result_set": {
    "current_page": 1,
    "total_objects": 2,
    "total_pages": 1,
    "limit": 100
  }
}
```

### create-group-role

```bash
yeedu platform-admin create-group-role -h
```

```bash
usage:  create-group-role [-h] [--tenant_id TENANT_ID] --group_id GROUP_ID --role_id
                          ROLE_ID [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to create-group-role.
  --group_id GROUP_ID   Provide Group Id to create-group-role.
  --role_id ROLE_ID     Provide Role Id to create-group-role.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-group-role example with all the required and optional arguments passed.

```bash
yeedu platform-admin create-group-role --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --group_id=1 --role_id=1
```

- Console output

```bash
{
  "group_roles_id": "3",
  "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
  "group_id": "1",
  "role_id": 1,
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T08:33:16.920Z",
  "from_date": "2024-06-14T08:33:16.920Z",
  "to_date": null
}
```

### delete-group-role

```bash
yeedu platform-admin delete-group-role -h
```

```bash
usage:  delete-group-role [-h] [--tenant_id TENANT_ID] --group_id GROUP_ID --role_id
                          ROLE_ID [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_id TENANT_ID
                        Provide Tenant Id to delete-group-role.
  --group_id GROUP_ID   Provide Group Id to delete-group-role.
  --role_id ROLE_ID     Provide Role Id to delete-group-role.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- delete-group-role example with all the required argument passed.

```bash
yeedu platform-admin delete-group-role --tenant_id="8ad4bd62-839f-4aa7-ba1e-c3112cbbf870" --group_id=15 --role_id=0
```

- Console output

```bash
{
  "message": "Deleted Group Role for the provided tenant ID: '8ad4bd62-839f-4aa7-ba1e-c3112cbbf870', group ID: 15, and role ID: 0."
}
```

# Admin

## User

| Command Name                            | Utility                                    |
| --------------------------------------- | ------------------------------------------ |
| [list-users](#list-users-3)             | To list all the users present in tenant.   |
| [search-users](#search-users-2)         | To search all the users present in tenant. |
| [get-user](#get-user)                   | To get information about a specific User.  |
| [get-user-roles](#get-user-roles-2)     | To get all the roles of a specific User.   |
| [list-users-roles](#list-users-roles-1) | To list all the Users Roles.               |
| [get-role-users](#get-role-users-1)     | To get all the users in a specific Role.   |
| [create-user-role](#create-user-role-1) | To create an User Role.                    |
| [delete-user-role](#delete-user-role-1) | To delete an User Role.                    |

### list-users

```bash
yeedu admin list-users -h
```

```bash
usage:  list-users [-h] [--page_number PAGE_NUMBER] [--limit LIMIT]
                   [--json-output [{pretty,default}]]
                   [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --page_number PAGE_NUMBER
                        To list users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-users example with optional arguments passed.

```bash
yeedu admin list-users --limit=1
```

- Console output

```bash
{
  "data": [
    {
      "user_id": 1,
      "username": "YSU0000",
      "display_name": "YSU0000",
      "email": "ysu0000@yeedu.com"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 1
  }
}
```

### search-users

```bash
yeedu admin search-users -h
```

```bash
usage:  search-users [-h] --username USERNAME
                     [--page_number PAGE_NUMBER] [--limit LIMIT]
                     [--json-output [{pretty,default}]]
                     [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --username USERNAME   Provide username to search matching users.
  --page_number PAGE_NUMBER
                        To search users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-users example with required and optional arguments passed.

```bash
yeedu admin search-users --username="YS"
```

- Console output

```bash
{
  "data": [
    {
      "user_id": 1,
      "username": "YSU0000",
      "user_roles": [
        "Platform Admin"
      ],
      "group_roles": [
        "Admin",
        "Can Manage Cluster",
        "User"
      ]
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-user

```bash
yeedu admin get-user -h
```

```bash
usage:  get-user [-h] --user_id USER_ID
                 [--json-output [{pretty,default}]]
                 [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --user_id USER_ID     Provide User Id to get information about a specific User.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-user example with the required argument passed.

```bash
yeedu admin get-user --user_id=1
```

- Console output

```bash
{
  "user_id": 1,
  "username": "YSU0000",
  "display_name": "YSU0000",
  "email": "ysu0000@yeedu.com",
  "from_date": "2024-06-13T11:29:51.951785+00:00",
  "to_date": "infinity"
}
```

### get-user-roles

```bash
yeedu admin get-user-roles -h
```

```bash
usage:  get-user-roles [-h] --user_id USER_ID
                       [--json-output [{pretty,default}]]
                       [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --user_id USER_ID     Provide User Id to get roles of a specific User.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-user-roles example with the required arguments '--user_id' passed.

```bash
yeedu admin get-user-roles --user_id=1
```

- Console output

```bash
{
  "user_id": 1,
  "username": "YSU0000",
  "email": "ysu0000@yeedu.com",
  "user_roles": [
    {
      "role_id": 3,
      "user_role": "Platform Admin"
    }
  ],
  "group_roles": [
    {
      "group_id": 1,
      "group_name": "yeedu-manager",
      "group_mail": null,
      "group_object_id": null,
      "group_type": null,
      "role_id": 2,
      "group_role": "Admin"
    },
    {
      "group_id": 1,
      "group_name": "yeedu-manager",
      "group_mail": null,
      "group_object_id": null,
      "group_type": null,
      "role_id": 1,
      "group_role": "Can Manage Cluster"
    },
    {
      "group_id": 1,
      "group_name": "yeedu-manager",
      "group_mail": null,
      "group_object_id": null,
      "group_type": null,
      "role_id": 0,
      "group_role": "User"
    }
  ],
  "from_date": "2024-06-13T11:29:51.951785+00:00",
  "to_date": "infinity"
}
```

### list-users-roles

```bash
yeedu admin list-users-roles -h
```

```bash
usage:  list-users-roles [-h] [--page_number PAGE_NUMBER]
                         [--limit LIMIT]
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --page_number PAGE_NUMBER
                        To list users roles for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of users roles. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-users-roles example with optional arguments passed.

```bash
yeedu admin list-users-roles
```

- Console output

```bash
{
  "data": [
    {
      "user_id": 1,
      "username": "YSU0000",
      "user_roles": [
        "Platform Admin"
      ],
      "group_roles": [
        "Admin",
        "Can Manage Cluster",
        "User"
      ]
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-role-users

```bash
yeedu admin get-role-users -h
```

```bash
usage:  get-role-users [-h] --role_id ROLE_ID
                       [--page_number PAGE_NUMBER] [--limit LIMIT]
                       [--json-output [{pretty,default}]]
                       [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --role_id ROLE_ID     Provide Role Id to get users in a specific Role.
  --page_number PAGE_NUMBER
                        To list users for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of users. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-role-users example with the required '--role_id' arguments passed.

```bash
yeedu admin get-role-users --role_id=3
```

- Console output

```bash
{
  "data": {
    "role_id": 3,
    "users": [
      {
        "user_id": 1,
        "username": "YSU0000",
        "display_name": "YSU0000",
        "email": "ysu0000@yeedu.com"
      }
    ]
  },
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### create-user-role

```bash
yeedu admin create-user-role -h
```

```bash
usage:  create-user-role [-h] --user_id USER_ID --role_id ROLE_ID
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --user_id USER_ID     Provide User Id to create-user-role.
  --role_id ROLE_ID     Provide Role Id to create-user-role.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-user-role example with all the required and optional arguments passed.

```bash
yeedu admin create-user-role --user_id=2 --role_id=1
```

- Console output

```bash
{
  "user_roles_id": "3",
  "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
  "user_id": "2",
  "role_id": 1,
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T08:42:08.226Z",
  "from_date": "2024-06-14T08:42:08.226Z",
  "to_date": null
}
```

### delete-user-role

```bash
yeedu admin delete-user-role -h
```

```bash
usage:  delete-user-role [-h] --user_id USER_ID --role_id ROLE_ID
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --user_id USER_ID     Provide User Id to delete-user-role.
  --role_id ROLE_ID     Provide Role Id to delete-user-role.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- delete-user-role example with all the required argument passed.

```bash
yeedu admin delete-user-role --user_id=2 --role_id=1
```

- Console output

```bash
{
  "message": "Deleted User Roles for the provided User Id: 2 and Role Id: 1."
}
```

## Group

| Command Name                              | Utility                                     |
| ----------------------------------------- | ------------------------------------------- |
| [list-groups](#list-groups-2)             | To list all the groups present in tenant.   |
| [search-groups](#search-groups-2)         | To search all the groups present in tenant. |
| [get-group](#get-group)                   | To get information about a specific Group.  |
| [get-group-roles](#get-group-roles-1)     | To get all the roles of a specific Group.   |
| [list-groups-roles](#list-groups-roles-1) | To list all the Groups Roles.               |
| [get-role-groups](#get-role-groups-1)     | To get all the groups in a specific Role.   |
| [create-group-role](#create-group-role-1) | To create a Group Role.                     |
| [delete-group-role](#delete-group-role-1) | To delete a group Role.                     |

### list-groups

```bash
yeedu admin list-groups -h
```

```bash
usage:  list-groups [-h] [--page_number PAGE_NUMBER] [--limit LIMIT]
                    [--json-output [{pretty,default}]]
                    [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --page_number PAGE_NUMBER
                        To list groups for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of groups. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-groups example with the optional argument passed.

```bash
yeedu admin list-groups
```

- Console output

```bash
{
  "data": [
    {
      "group_id": 1,
      "group_name": "yeedu-manager",
      "group_mail": null,
      "group_object_id": null,
      "group_type": null
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### search-groups

```bash
yeedu admin search-groups -h
```

```bash
usage:  search-groups [-h] --groupname GROUPNAME
                      [--page_number PAGE_NUMBER] [--limit LIMIT]
                      [--json-output [{pretty,default}]]
                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --groupname GROUPNAME
                        Provide groupname to search matching groups.
  --page_number PAGE_NUMBER
                        To search groups for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to search number of groups. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- search-groups example with required and optional arguments passed.

```bash
yeedu admin search-groups --groupname="yeed"
```

- Console output

```bash
{
  "data": [
    {
      "group_id": 1,
      "group_name": "yeedu-manager",
      "group_mail": null,
      "group_type": null,
      "group_object_id": null,
      "roles": [
        "Admin",
        "Can Manage Cluster",
        "User"
      ]
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-group

```bash
yeedu admin get-group -h
```

```bash
usage:  get-group [-h] --group_id GROUP_ID
                  [--json-output [{pretty,default}]]
                  [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --group_id GROUP_ID   Provide Group Id to get information about a specific Group.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-group example with the required argument '--group_id' passed.

```bash
yeedu admin get-group --group_id=1
```

- Console output

```bash
{
  "group_id": 1,
  "group_name": "yeedu-manager",
  "group_object_id": null,
  "group_type": null,
  "from_date": "2024-06-13T11:29:51.951785+00:00",
  "to_date": "infinity"
}
```

### get-group-roles

```bash
yeedu admin get-group-roles -h
```

```bash
usage:  get-group-roles [-h] --group_id GROUP_ID
                        [--json-output [{pretty,default}]]
                        [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --group_id GROUP_ID   Provide Group Id to get roles of a specific Group.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-group-roles example with the required argument '--group_id' passed.

```bash
yeedu admin get-group-roles --group_id=1
```

- Console output

```bash
{
  "group_id": 1,
  "group_name": "yeedu-manager",
  "group_type": null,
  "roles": [
    "Admin",
    "Can Manage Cluster",
    "User"
  ]
}
```

### list-groups-roles

```bash
yeedu admin list-groups-roles -h
```

```bash
usage:  list-groups-roles [-h] [--page_number PAGE_NUMBER] [--limit LIMIT]
                          [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --page_number PAGE_NUMBER
                        To list groups roles for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of groups roles. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-groups-roles example without any optional arguments passed.

```bash
yeedu admin list-groups-roles
```

- Console output

```bash
{
  "data": [
    {
      "group_id": 1,
      "group_name": "yeedu-manager",
      "group_mail": null,
      "group_type": null,
      "group_object_id": null,
      "roles": [
        "Admin",
        "Can Manage Cluster",
        "User"
      ]
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### get-role-groups

```bash
yeedu admin get-role-groups -h
```

```bash
usage:  get-role-groups [-h] --role_id ROLE_ID [--json-output [{pretty,default}]]
                        [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --role_id ROLE_ID     Provide Role Id to get groups in a specific Role.
  --page_number PAGE_NUMBER
                        To list groups for a specific page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of groups. (default: 100)

  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-role-groups example with the required argument '--role_id' passed.

```bash
yeedu admin get-role-groups --role_id=2
```

- Console output

```bash
{
  "data": {
    "role_id": 2,
    "groups": [
      {
        "group_id": 1,
        "group_name": "yeedu-manager",
        "group_mail": null,
        "group_object_id": null,
        "group_type": null
      }
    ]
  },
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### create-group-role

```bash
yeedu admin create-group-role -h
```

```bash
usage:  create-group-role [-h] --group_id GROUP_ID --role_id ROLE_ID
                          [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --group_id GROUP_ID   Provide Group Id to create-group-role.
  --role_id ROLE_ID     Provide Role Id to create-group-role.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- create-group-role example with all the required arguments passed.

```bash
yeedu admin create-group-role --group_id=15 --role_id=0
```

- Console output

```bash
{
  "group_roles_id": "5",
  "tenant_id": "8ad4bd62-839f-4aa7-ba1e-c3112cbbf870",
  "group_id": "15",
  "role_id": 0,
  "created_by_user_id": "1",
  "modified_by_user_id": "1",
  "last_update_date": "2024-06-14T08:46:04.846Z",
  "from_date": "2024-06-14T08:46:04.846Z",
  "to_date": null
}
```

### delete-group-role

```bash
yeedu admin delete-group-role -h
```

```bash
usage:  delete-group-role [-h] --group_id GROUP_ID --role_id ROLE_ID
                          [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --group_id GROUP_ID   Provide Group Id to delete-group-role.
  --role_id ROLE_ID     Provide Role Id to delete-group-role.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- delete-group-role example with all the required argument passed.

```bash
yeedu admin delete-group-role --group_id=15 --role_id=0
```

- Console output

```bash
{
  "message": "Deleted Group Role for the provided group ID: 15, and role ID: 0."
}
```

# Token

| Command Name                    | Utility                                      |
| ------------------------------- | -------------------------------------------- |
| [create](#create-2)             | Generate a Yeedu session token.              |
| [list](#list-4)                 | List the token details.                      |
| [delete](#delete)               | Revoke a particular Yeedu session token.     |

### create

```bash
yeedu token create -h
```

```bash
usage:  create [-h] [--description DESCRIPTION]
               [--timeout [TIMEOUT]]
               [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --description DESCRIPTION
                        Provide description for the session to be used
                        for.
  --timeout [TIMEOUT]   Provide token expiration timeout Example: --timeout=24h 
                        or 2 days or 1700s,--timeout=infinity 
                        (infinity for no expiration time) 
                        to generate Yeedu Token. (default: 30 days)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set
                        to 'true'. (default: false)
```

- token create example.

```bash
yeedu token create --description="Yeedu session token" --timeout=48h
```

- Console output

```bash
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyOCwiaWF0IjoxNzQxMTg2MDA3LCJleHAiOjE3NDEzNTg4MDd9.eHKy_afdIkIOaJ-dmtJUb5TpYkF3CtYO8hsottdFg6I"
}
```

### list

```bash
yeedu token list -h
```

```bash
usage:  list [-h] [--page_number PAGE_NUMBER] [--limit LIMIT]
             [--json-output [{pretty,default}]]
             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --page_number PAGE_NUMBER
                        To list token details for a specific
                        page_number. (default: 1)
  --limit LIMIT         Provide limit to list number of token details.
                        (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set
                        to 'true'. (default: false)
```

- list example.

```bash
yeedu token list
```

- Console output

```bash
{
  "data": [
    {
      "token_id": 1,
      "description": "Yeedu session token",
      "tenant_id": "2419786c-8568-4f20-a01b-d66a0f7e8ca2",
      "created_by": {
        "user_id": 28,
        "username": "yeedu@yeedu.com"
      },
      "modified_by": {
        "user_id": 28,
        "username": "yeedu@yeedu.com"
      },
      "expiry_time": "2025-03-07T14:46:47.538+00:00"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### delete

```bash
yeedu token delete -h
```

```bash
usage:  delete [-h] --token_id TOKEN_ID [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --token_id TOKEN_ID   Provide Token Id to revoke a specific token.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default:
                        pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to
                        'true'. (default: false)
```

- delete token example.

```bash
yeedu token delete --token_id=1
```

- Console output

```bash
{
  "message": "Successfully revoked the session for the provided token Id: 1."
}
```

# Secret
The secret command in **Yeedu CLI** allows users to manage secrets at different levels: **tenant secrets, workspace secrets, and user secrets**.

| Command Name                                        | Utility                                  |
| --------------------------------------------------- | ---------------------------------------- |
| [create-tenant-secret](#create-tenant-secret)       | Create a new tenant secret.              |
| [edit-tenant-secret](#edit-tenant-secret)           | Edit an existing tenant secret.          |
| [list-tenant-secrets](#list-tenant-secrets)         | Retrieve a list of tenant secrets.       |
| [delete-tenant-secret](#delete-tenant-secret)       | Delete a tenant secret.                  |
| [create-workspace-secret](#create-workspace-secret) | Create a new workspace secret.           |
| [edit-workspace-secret](#edit-workspace-secret)     | Edit an existing workspace secret.       |
| [list-workspace-secrets](#list-workspace-secrets)   | Retrieve a list of workspace secrets.    |
| [delete-workspace-secret](#delete-workspace-secret) | Delete a workspace secret.               |
| [create-user-secret](#create-user-secret)           | Create a new user secret.                |
| [edit-user-secret](#edit-user-secret)               | Edit an existing user secret.            |
| [list-user-secrets](#list-user-secrets)             | Retrieve a list of user secrets.         |
| [delete-user-secret](#delete-user-secret)           | Delete a user secret.                    |


## Tenant Secrets

### create-tenant-secret

```bash
yeedu secret create-tenant-secret -h
```

```bash
usage:  create-tenant-secret [-h] --name NAME [--description DESCRIPTION] --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT
                             VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT} [--json-output [{pretty,default}]]
                             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name NAME           Specify the identifier of the secret.
  --description DESCRIPTION
                        Provide a description for the secret.
  --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                        Specify the type of authentication secret.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Tenant Create Secret Example

```bash
yeedu secret create-tenant-secret --name "tenantDB" --description "Tenant Database Secret" --secret_type "HIVE BASIC" --username "tenant_user" --password "tenant_pass"
```

- Console Output
```json
{
  "tenant_secret_id": "20",
  "name": "tenantDB",
  "description": "Tenant Database Secret",
  "lookup_secret_type_id": "2",
  "created_by_user_id": "25",
  "modified_by_user_id": "25",
  "last_update_date": "2025-04-03T07:32:24.621Z",
  "from_date": "2025-04-03T07:32:24.621Z",
  "to_date": null
}
```


### Edit Tenant Secret


```bash
yeedu secret edit-tenant-secret -h
```

```bash
usage:  edit-tenant-secret [-h] --tenant_secret_id TENANT_SECRET_ID [--description DESCRIPTION] --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                           [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --tenant_secret_id TENANT_SECRET_ID
                        ID of the tenant secret to be updated.
  --description DESCRIPTION
                        Provide a description for the secret.
  --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                        Specify the type of authentication secret.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Edit Tenant Secret Example
```bash
yeedu secret edit-tenant-secret --tenant_secret_id 23 --secret_type "HIVE BASIC" --username user --password pass
```
- Console Output
```json
{
  "tenant_secret_id": "23",
  "name": "tenantSecret",
  "description": "Tenant Database Secret",
  "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
  "created_by_user_id": "25",
  "modified_by_user_id": "25",
  "last_update_date": "2025-04-03T10:09:08.268Z",
  "from_date": "2025-04-03T10:07:40.028Z",
  "to_date": null
}
```

### list-tenant-secrets

```bash
yeedu secret list-tenant-secrets -h
```

```bash
usage: list-tenant-secrets [-h] [--page_number PAGE_NUMBER] [--limit LIMIT]
                           [--json-output {pretty,default}]
                           [--yaml-output {true,false}]
                           
options:
  -h, --help            show this help message and exit
  --page_number PAGE_NUMBER
                        Specifies the page number for results pagination. (default: 1)
  --limit LIMIT         Specifies the maximum number of configurations to list per page. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)

```

- Tenant List Secrets Example
```bash
yeedu secret list-tenant-secrets --page_number 1 --limit 1
```

- Console Output
```json
{
  "data": [
    {
      "tenant_secret_id": 22,
      "name": "dasdbtok1",
      "description": "asd",
      "secret_type": "DATABRICKS UNITY TOKEN",
      "tenant": {
        "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
        "name": "ui_tenant",
        "description": null
      },
      "created_by": {
        "user_id": 25,
        "username": "yeedu@yeedu.com"
      },
      "modified_by": {
        "user_id": 25,
        "username": "yeedu@yeedu.com"
      },
      "last_update_date": "2025-04-03T07:41:16.310727+00:00",
      "from_date": "2025-04-03T07:41:16.310727+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 21,
    "total_pages": 21,
    "limit": 1,
    "next_page": 2
  }
}
```

### search-tenant-secrets

```bash
yeedu secret search-tenant-secrets -h
```

```bash
usage:  search-tenant-secrets [-h] --secret_name SECRET_NAME
                              [--secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}]
                              [--page_number PAGE_NUMBER] [--limit LIMIT] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --secret_name SECRET_NAME
                        ID of the tenant secret to search for.
  --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                        Type of the tenant secret to search for.
  --page_number PAGE_NUMBER
                        Specifies the page number for results pagination. (default: 1)
  --limit LIMIT         Specifies the maximum number of configurations to list per page. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Tenant Search Secrets Example
```bash
yeedu secret search-tenant-secrets --secret_name "env1" --secret_type "ENVIRONMENT VARIABLE"
```

- Console Output
```json
{
  "data": [
    {
      "tenant_secret_id": 2,
      "name": "env1",
      "description": "as",
      "secret_type": "ENVIRONMENT VARIABLE",
      "tenant": {
        "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
        "name": "ui_tenant",
        "description": null
      },
      "created_by": {
        "user_id": 25,
        "username": "yeedu@yeedu.com"
      },
      "modified_by": {
        "user_id": 25,
        "username": "yeedu@yeedu.com"
      },
      "last_update_date": "2025-04-01T15:36:57.313933+00:00",
      "from_date": "2025-04-01T15:36:57.313933+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### delete-tenant-secret

```bash
yeedu secret delete-tenant-secret -h
```

```bash
usage: delete-tenant-secret [-h] --tenant_secret_id SECRET_ID
                            [--json-output {pretty,default}]
                            [--yaml-output {true,false}]
                            
options:
  -h, --help            show this help message and exit
  --tenant_secret_id TENANT_SECRET_ID
                        ID of the tenant secret to be deleted.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)

```

- Tenant Delete Secret Example
```bash
yeedu secret delete-tenant-secret --tenant_secret_id 8
```

- Console Output
```json
{
  "message": "Deleted tenant secret ID: 8."
}
```

## Workspace Secrets

### create-workspace-secret

```bash
yeedu secret create-workspace-secret -h
```

```bash
usage:  create-workspace-secret [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] --name NAME [--description DESCRIPTION]
                                --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT} [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Specify the Workspace ID.
  --workspace_name WORKSPACE_NAME
                        Specify the Workspace Name
  --name NAME           Specify the identifier of the secret.
  --description DESCRIPTION
                        Provide a description for the secret.
  --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                        Specify the type of authentication secret.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Create Workspace Secret Example
```bash
yeedu secret create-workspace-secret --workspace_id 10 --name "WorkspaceSecret" --description "Workspace Secret" --secret_type "ENVIRONMENT VARIABLE" --value "DB_PASSWORD=securePass"
```

- Console Output
```json
{
  "workspace_secret_id": "9",
  "description": "Workspace Secret",
  "name": "WorkspaceSecret",
  "lookup_secret_type_id": "4",
  "created_by_user_id": "25",
  "modified_by_user_id": "25",
  "last_update_date": "2025-04-03T08:27:20.800Z",
  "from_date": "2025-04-03T08:27:20.800Z",
  "to_date": null
}
```

### edit-workspace-secret
```bash
yeedu secret edit-workspace-secret -h
```

```bash
usage:  edit-workspace-secret [-h] --workspace_secret_id WORKSPACE_SECRET_ID [--workspace_id WORKSPACE_ID]
                              [--workspace_name WORKSPACE_NAME] [--description DESCRIPTION] --secret_type {HIVE KERBEROS,HIVE
                              BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                              [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_secret_id WORKSPACE_SECRET_ID
                        ID of the workspace secret to be updated.
  --workspace_id WORKSPACE_ID
                        Specify the Workspace ID.
  --workspace_name WORKSPACE_NAME
                        Specify the Workspace Name
  --description DESCRIPTION
                        Provide a description for the secret.
  --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                        Specify the type of authentication secret.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Edit Workspace Secret Example
```bash
yeedu secret edit-workspace-secret --workspace_id 10 --workspace_secret_id 12 --description "Workspace Secretss" --secret_type "ENVIRONMENT VARIABLE" --value "DB_PASSWORD=securePasswordasdf"
```

- Console Output
```json
{
  "workspace_secret_id": "12",
  "description": "Workspace Secretss",
  "name": "WorkspaceSecretUpdate",
  "vault_path": "yeedu/secrets/workspace/10/12",
  "lookup_secret_type_id": "4",
  "created_by_user_id": "25",
  "modified_by_user_id": "25",
  "last_update_date": "2025-04-03T10:05:18.227Z",
  "from_date": "2025-04-03T10:05:07.143Z",
  "to_date": null
}
```


### list-workspace-secrets

```bash
yeedu secret list-workspace-secrets -h
```

```bash
usage:  list-workspace-secrets [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] [--page_number PAGE_NUMBER]
                               [--limit LIMIT] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Specify the workspace ID.
  --workspace_name WORKSPACE_NAME
                        Specify the workspace name.
  --page_number PAGE_NUMBER
                        Specifies the page number for results pagination. (default: 1)
  --limit LIMIT         Specifies the maximum number of configurations to list per page. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- List Workspace Secrets Example
```bash
yeedu secret list-workspace-secrets --page_number 1 --limit 1 --workspace_id 1
```

- Console Output
```json
{
  "data": [
    {
      "workspace_secret_id": 7,
      "description": null,
      "name": "env",
      "secret_type": "ENVIRONMENT VARIABLE",
      "workspace": {
        "workspace_id": 1,
        "name": "testing_workspace",
        "description": null
      },
      "created_by": {
        "user_id": 25,
        "username": "yeedu@yeedu.com"
      },
      "modified_by": {
        "user_id": 25,
        "username": "yeedu@yeedu.com"
      },
      "last_update_date": "2025-04-02T12:43:53.404536+00:00",
      "from_date": "2025-04-02T12:43:53.404536+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 5,
    "total_pages": 5,
    "limit": 1,
    "next_page": 2
  }
}
```

### search-workspace-secrets

```bash
yeedu secret search-workspace-secrets -h
```

```bash
usage:  search-workspace-secrets [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] --secret_name SECRET_NAME
                                 [--secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}]
                                 [--page_number PAGE_NUMBER] [--limit LIMIT] [--json-output [{pretty,default}]]
                                 [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Specify the workspace ID.
  --workspace_name WORKSPACE_NAME
                        Specify the workspace name.
  --secret_name SECRET_NAME
                        ID of the tenant secret to search for.
  --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                        Type of the tenant secret to search for.
  --page_number PAGE_NUMBER
                        Specifies the page number for results pagination. (default: 1)
  --limit LIMIT         Specifies the maximum number of configurations to list per page. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Search Workspace Secrets Example
```bash
yeedu secret search-workspace-secrets --secret_name "env" --secret_type "ENVIRONMENT VARIABLE" --workspace_id 1
```

- Console Output
```json
{
  "data": [
    {
      "workspace_secret_id": 7,
      "description": null,
      "name": "env",
      "secret_type": "ENVIRONMENT VARIABLE",
      "workspace": {
        "workspace_id": 1,
        "name": "testing_workspace",
        "description": null
      },
      "created_by": {
        "user_id": 25,
        "username": "yeedu@yeedu.com"
      },
      "modified_by": {
        "user_id": 25,
        "username": "yeedu@yeedu.com"
      },
      "last_update_date": "2025-04-02T12:43:53.404536+00:00",
      "from_date": "2025-04-02T12:43:53.404536+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### delete-workspace-secret

```bash
yeedu secret delete-workspace-secret -h
```

```bash
usage:  delete-workspace-secret [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] --workspace_secret_id WORKSPACE_SECRET_ID
                                [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Specify the workspace ID.
  --workspace_name WORKSPACE_NAME
                        Specify the workspace name.
  --workspace_secret_id WORKSPACE_SECRET_ID
                        ID of the workspace secret to be deleted.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Delete Workspace Secret Example
```bash
yeedu secret delete-workspace-secret --workspace_id 1 --workspace_secret_id 3
```

- Console Output
```json
{
  "message": "Deleted workspace secret id: 3."
}
```

## User Secrets

### create-user-secret

```bash
yeedu secret create-user-secret -h
```

```bash
usage:  create-user-secret [-h] --name NAME [--description DESCRIPTION] --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY
                           TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                           [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name NAME           Specify the identifier of the secret.
  --description DESCRIPTION
                        Provide a description for the secret.
  --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                        Specify the type of authentication secret.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Create User Secret Example:**
```bash
yeedu secret create-user-secret --name "userToken" --description "User API Token" --secret_type "DATABRICKS UNITY TOKEN" --token "user-secret-token"
```

- Console Output
```json
{
  "user_secret_id": "7",
  "description": "User API Token",
  "name": "userToken",
  "lookup_secret_type_id": "3",
  "created_by_user_id": "25",
  "modified_by_user_id": "25",
  "last_update_date": "2025-04-03T10:10:49.888Z",
  "from_date": "2025-04-03T10:10:49.888Z",
  "to_date": null
}
```


### edit-user-secret

```bash
yeedu secret edit-user-secret -h
```

```bash
usage:  edit-user-secret [-h] --user_secret_id USER_SECRET_ID [--description DESCRIPTION] --secret_type {HIVE KERBEROS,HIVE
                         BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                         [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --user_secret_id USER_SECRET_ID
                        ID of the user secret to be updated.
  --description DESCRIPTION
                        Provide a description for the secret.
  --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                        Specify the type of authentication secret.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Edit User Secret Example:**
```bash
yeedu secret edit-user-secret --description "User API Token" --secret_type "DATABRICKS UNITY TOKEN" --token "user-secret-tokenchangingthis" --user_secret_id 7
```

- Console Output
```json
{
  "user_secret_id": "7",
  "description": "User API Token",
  "name": "userToken",
  "lookup_secret_type_id": "3",
  "created_by_user_id": "25",
  "last_update_date": "2025-04-03T10:11:41.342Z",
  "from_date": "2025-04-03T10:10:49.888Z",
  "to_date": null
}
```

### list-user-secrets

```bash
yeedu secret list-user-secrets -h
```

```bash
usage:  list-user-secrets [-h] [--page_number PAGE_NUMBER] [--limit LIMIT]
                          [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --page_number PAGE_NUMBER
                        Specifies the page number for results pagination. (default: 1)
  --limit LIMIT         Specifies the maximum number of configurations to list per page. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- List User Secrets Example
```bash
yeedu secret list-user-secrets --page_number 1 --limit 1
```

- Console Output
```json
{
  "data": [
    {
      "user_secret_id": 7,
      "name": "userToken",
      "description": "User API Token",
      "secret_type": "DATABRICKS UNITY TOKEN",
      "created_by": {
        "user_id": 25,
        "username": "yeedu@yeedu.com"
      },
      "modified_by": {
        "user_id": 25,
        "username": "yeedu@yeedu.com"
      },
      "last_update_date": "2025-04-03T10:11:41.342+00:00",
      "from_date": "2025-04-03T10:10:49.888885+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 5,
    "total_pages": 5,
    "limit": 1,
    "next_page": 2
  }
}
```

### list-user-secrets

```bash
yeedu secret search-user-secrets -h
```

```bash
usage:  search-user-secrets [-h] --secret_name SECRET_NAME
                            [--secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}]
                            [--page_number PAGE_NUMBER] [--limit LIMIT] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --secret_name SECRET_NAME
                        ID of the tenant secret to search for.
  --secret_type {HIVE KERBEROS,HIVE BASIC,DATABRICKS UNITY TOKEN,ENVIRONMENT VARIABLE,AWS ACCESS SECRET KEY PAIR,AZURE SERVICE PRINCIPAL,GOOGLE SERVICE ACCOUNT}
                        Type of the tenant secret to search for.
  --page_number PAGE_NUMBER
                        Specifies the page number for results pagination. (default: 1)
  --limit LIMIT         Specifies the maximum number of configurations to list per page. (default: 100)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Search User Secrets Example
```bash
yeedu secret search-user-secrets --secret_name user --secret_type "DATABRICKS UNITY TOKEN"
```

- Console Output
```json
{
  "data": [
    {
      "user_secret_id": 7,
      "name": "userToken",
      "description": "User API Token",
      "secret_type": "DATABRICKS UNITY TOKEN",
      "created_by": {
        "user_id": 25,
        "username": "yeedu@yeedu.com"
      },
      "modified_by": {
        "user_id": 25,
        "username": "yeedu@yeedu.com"
      },
      "last_update_date": "2025-04-03T10:11:41.342+00:00",
      "from_date": "2025-04-03T10:10:49.888885+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```

### delete-user-secret

```bash
yeedu secret delete-user-secret -h
```

```bash
usage:  delete-user-secret [-h] --user_secret_id USER_SECRET_ID
                           [--json-output [{pretty,default}]]
                           [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --user_secret_id USER_SECRET_ID
                        ID of the user secret to be deleted.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Delete User Secret Example
```bash
yeedu secret delete-user-secret --user_secret_id 7
```

- Console Output
```json
{
  "message": "Deleted user secret id: 7."
}
```

# Metastore Catalog Operations

## Secret Management

| Command Name                        | Utility                                                                          |
|-------------------------------------|-----------------------------------------------------------------------------------|
| [associate-tenant-secret](#associate-tenant-secret)         | To associate a secret with a tenant.                      |
| [associate-workspace-secret](#associate-workspace-secret)   | To associate a secret with a workspace.                   |
| [associate-user-secret](#associate-user-secret)             | To associate a secret with a user.                        |
| [update-tenant-secret](#update-tenant-secret)               | To update a secret from a tenant.                         |
| [update-workspace-secret](#update-workspace-secret)         | To update a secret from a workspace.                      |
| [update-user-secret](#update-user-secret)                   | To update a secret from a user.                           |
| [deassociate-tenant-secret](#deassociate-tenant-secret)     | To deassociate a secret from a tenant.                    |
| [deassociate-workspace-secret](#deassociate-workspace-secret)| To deassociate a secret from a workspace.                |
| [deassociate-user-secret](#deassociate-user-secret)         | To deassociate a secret from a user.                      |
| [list-tenant-associated-secrets](#list-tenant-associated-secrets) | To list secrets associated with a tenant.           |
| [list-workspace-associated-secrets](#list-workspace-associated-secrets) | To list secrets associated with a workspace.  |
| [list-user-associated-secrets](#list-user-associated-secrets)     | To list secrets associated with a user.             |

### Associate Tenant Secret
```bash
yeedu metastore-catalog link-tenant-secret -h
```
```bash
usage:  link-tenant-secret [-h] --metastore_catalog_id METASTORE_CATALOG_ID
                           [--metastore_secrets_tenant_id METASTORE_SECRETS_TENANT_ID]
                           [--object_storage_secrets_tenant_id OBJECT_STORAGE_SECRETS_TENANT_ID]
                           [--json-output [{pretty,default}]]
                           [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        ID of the metastore catalog to which the tenant secret
                        will be linked.
  --metastore_secrets_tenant_id METASTORE_SECRETS_TENANT_ID
                        ID of the tenant secret used to access the metastore
                        service.
  --object_storage_secrets_tenant_id OBJECT_STORAGE_SECRETS_TENANT_ID
                        ID of the tenant secret used to access the backing object
                        storage.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```
- Example:
```bash
yeedu metastore-catalog link-tenant-secret --metastore_catalog_id 13 --metastore_secrets_tenant_id 6  --object_storage_secrets_tenant_id 1
```
- Console Output:
```json
{
  "metastore_catalog_secrets_tenant_id": "6",
  "metastore_catalog_id": "13",
  "metastore_secrets_tenant_id": "6",
  "object_storage_secrets_tenant_id": "1",
  "created_by_user_id": "6",
  "modified_by_user_id": "20",
  "last_update_date": "2025-04-14T07:59:38.489Z",
  "from_date": "2025-02-21T09:08:46.557Z",
  "to_date": null
}
```

### Associate Workspace Secret
```bash
yeedu metastore-catalog link-workspace-secret -h
```
```bash
usage:  link-workspace-secret [-h] --metastore_catalog_id METASTORE_CATALOG_ID
                              --metastore_secrets_workspace_id
                              METASTORE_SECRETS_WORKSPACE_ID
                              --object_storage_secrets_workspace_id
                              OBJECT_STORAGE_SECRETS_WORKSPACE_ID
                              [--json-output [{pretty,default}]]
                              [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        ID of the metastore catalog to which the workspace secret
                        will be linked.
  --metastore_secrets_workspace_id METASTORE_SECRETS_WORKSPACE_ID
                        ID of the workspace secret used to access the metastore
                        service.
  --object_storage_secrets_workspace_id OBJECT_STORAGE_SECRETS_WORKSPACE_ID
                        ID of the workspace secret used to access the backing
                        object storage.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```
- Example:
```bash
yeedu metastore-catalog link-workspace-secret --metastore_catalog_id 13 --metastore_secrets_workspace_id 13 --object_storage_secrets_workspace_id 9
```
- Console Output:
```json
{
  "metastore_catalog_secrets_workspace_id": "2",
  "metastore_catalog_id": "13",
  "metastore_secrets_workspace_id": "13",
  "object_storage_secrets_workspace_id": "9",
  "created_by_user_id": "20",
  "modified_by_user_id": "20",
  "last_update_date": "2025-04-14T08:05:51.438Z",
  "from_date": "2025-04-14T08:05:51.438Z",
  "to_date": null
}
```

### Associate User Secret
```bash
yeedu metastore-catalog link-user-secret -h
```
```bash
usage:  link-user-secret [-h] --metastore_catalog_id METASTORE_CATALOG_ID
                         [--metastore_secrets_user_id METASTORE_SECRETS_USER_ID]
                         [--object_storage_secrets_user_id OBJECT_STORAGE_SECRETS_USER_ID]
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        ID of the metastore catalog to which the user secret will
                        be linked.
  --metastore_secrets_user_id METASTORE_SECRETS_USER_ID
                        ID of the user secret used to access the metastore
                        service.
  --object_storage_secrets_user_id OBJECT_STORAGE_SECRETS_USER_ID
                        ID of the user secret used to access the backing object
                        storage.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)

```
- Example:
```bash
yeedu metastore-catalog link-user-secret --metastore_catalog_id=13 --metastore_secrets_user_id=36 --object_storage_secrets_user_id=38

```
- Console Output:
```json
{
  "metastore_catalog_secrets_user_id": "3",
  "metastore_catalog_id": "13",
  "metastore_secrets_user_id": "36",
  "object_storage_secrets_user_id": "38",
  "created_by_user_id": "20",
  "modified_by_user_id": "20",
  "last_update_date": "2025-04-14T08:11:20.555Z",
  "from_date": "2025-04-14T08:11:20.555Z",
  "to_date": null
}

```

### Update Tenant Secret
```bash
yeedu metastore-catalog update-tenant-secret -h
```
```bash
usage:  update-tenant-secret [-h] --metastore_catalog_secret_tenant_id METASTORE_CATALOG_SECRET_TENANT_ID [--metastore_secrets_tenant_id METASTORE_SECRETS_TENANT_ID]
                             [--object_storage_secrets_tenant_id OBJECT_STORAGE_SECRETS_TENANT_ID] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_secret_tenant_id METASTORE_CATALOG_SECRET_TENANT_ID
                        ID of the metastore catalog for which the tenant secret link should be updated.
  --metastore_secrets_tenant_id METASTORE_SECRETS_TENANT_ID
                        Updated tenant secret ID used to access the metastore service.
  --object_storage_secrets_tenant_id OBJECT_STORAGE_SECRETS_TENANT_ID
                        Updated tenant secret ID used to access the object storage.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)


options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        ID of the metastore catalog to which the tenant secret
                        will be linked.
  --metastore_secrets_tenant_id METASTORE_SECRETS_TENANT_ID
                        ID of the tenant secret used to access the metastore
                        service.
  --object_storage_secrets_tenant_id OBJECT_STORAGE_SECRETS_TENANT_ID
                        ID of the tenant secret used to access the backing object
                        storage.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```
- Example:
```bash
yeedu metastore-catalog update-tenant-secret --metastore_catalog_secret_tenant_id 6 --object_storage_secrets_tenant_id 2
```
- Console Output:
```json
{
  "metastore_catalog_secrets_tenant_id": "6",
  "metastore_catalog_id": "13",
  "metastore_secrets_tenant_id": "6",
  "object_storage_secrets_tenant_id": "2",
  "created_by_user_id": "6",
  "modified_by_user_id": "20",
  "last_update_date": "2025-04-14T09:34:38.012Z",
  "from_date": "2025-02-21T09:08:46.557Z",
  "to_date": null
}

```

### Update Workspace Secret
```bash
yeedu metastore-catalog update-workspace-secret -h
```
```bash
usage:  update-workspace-secret [-h] --metastore_catalog_secret_workspace_id METASTORE_CATALOG_SECRET_WORKSPACE_ID --metastore_secrets_workspace_id METASTORE_SECRETS_WORKSPACE_ID
                                --object_storage_secrets_workspace_id OBJECT_STORAGE_SECRETS_WORKSPACE_ID [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_secret_workspace_id METASTORE_CATALOG_SECRET_WORKSPACE_ID
                        ID of the metastore catalog whose workspace secret will be updated.
  --metastore_secrets_workspace_id METASTORE_SECRETS_WORKSPACE_ID
                        Updated workspace secret ID for the metastore service.
  --object_storage_secrets_workspace_id OBJECT_STORAGE_SECRETS_WORKSPACE_ID
                        Updated workspace secret ID for object storage access.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```
- Example:
```bash
yeedu metastore-catalog update-tenant-secret --metastore_catalog_secret_tenant_id 6 --object_storage_secrets_tenant_id 2

```
- Console Output:
```json
{
  "metastore_catalog_secrets_tenant_id": "6",
  "metastore_catalog_id": "13",
  "metastore_secrets_tenant_id": "6",
  "object_storage_secrets_tenant_id": "2",
  "created_by_user_id": "6",
  "modified_by_user_id": "20",
  "last_update_date": "2025-04-14T09:38:39.950Z",
  "from_date": "2025-02-21T09:08:46.557Z",
  "to_date": null
}
```

### Update User Secret
```bash
yeedu metastore-catalog update-user-secret -h
```
```bash
usage:  update-user-secret [-h] --metastore_catalog_secret_user_id METASTORE_CATALOG_SECRET_USER_ID [--metastore_secrets_user_id METASTORE_SECRETS_USER_ID]
                           [--object_storage_secrets_user_id OBJECT_STORAGE_SECRETS_USER_ID] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_secret_user_id METASTORE_CATALOG_SECRET_USER_ID
                        ID of the metastore catalog for which the user secret link should be updated.
  --metastore_secrets_user_id METASTORE_SECRETS_USER_ID
                        Updated user secret ID used to access the metastore service.
  --object_storage_secrets_user_id OBJECT_STORAGE_SECRETS_USER_ID
                        Updated user secret ID used to access the object storage.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)

```
- Example:
```bash
yeedu metastore-catalog update-user-secret --metastore_catalog_secret_user_id 3 --object_storage_secrets_user_id 38

```
- Console Output:
```json
{
  "metastore_catalog_secrets_workspace_id": "3",
  "metastore_catalog_id": "13",
  "metastore_secrets_workspace_id": "36",
  "object_storage_secrets_workspace_id": "38",
  "created_by_user_id": "20",
  "modified_by_user_id": "20",
  "last_update_date": "2025-04-14T09:46:25.248Z",
  "from_date": "2025-04-14T08:11:20.555Z",
  "to_date": null
}

```


### Deassociate Tenant Secret
```bash
yeedu metastore-catalog unlink-tenant-secret -h
```
```bash
usage:  unlink-tenant-secret [-h] --metastore_catalog_secret_tenant_id
                             METASTORE_CATALOG_SECRET_TENANT_ID
                             [--json-output [{pretty,default}]]
                             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_secret_tenant_id METASTORE_CATALOG_SECRET_TENANT_ID
                        ID of the tenant secret to be unlinked from the metastore
                        catalog.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```
- Example:
```bash
yeedu metastore-catalog unlink-tenant-secret --metastore_catalog_secret_tenant_id 6
```
- Console Output:
```json
{
  "message": "Deleted Metastore Catalog tenant secret: 6"
}
```

### Deassociate Workspace Secret
```bash
yeedu metastore-catalog unlink-workspace-secret -h
```
```bash
usage:  unlink-workspace-secret [-h] --metastore_catalog_secret_workspace_id
                                METASTORE_CATALOG_SECRET_WORKSPACE_ID
                                [--json-output [{pretty,default}]]
                                [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_secret_workspace_id METASTORE_CATALOG_SECRET_WORKSPACE_ID
                        Secret mapping ID to be unlinked.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)

```
- Example:
```bash
yeedu metastore-catalog unlink-workspace-secret --metastore_catalog_secret_workspace_id 2
```
- Console Output:
```json
{
  "message": "Deleted Metastore Catalog workspace secret: 2"
}
```

### Deassociate User Secret
```bash
yeedu metastore-catalog unlink-user-secret -h
```
```bash
usage:  unlink-user-secret [-h] --metastore_catalog_secret_user_id
                           METASTORE_CATALOG_SECRET_USER_ID
                           [--json-output [{pretty,default}]]
                           [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_secret_user_id METASTORE_CATALOG_SECRET_USER_ID
                        ID of the user secret to be unlinked from the metastore
                        catalog.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)

```
- Example:
```bash
yeedu metastore-catalog unlink-user-secret --metastore_catalog_secret_user_id 3
```
- Console Output:
```json
{
  "message": "Deleted Metastore Catalog user secret: 3"
}
```

### List Tenant Associated Secrets
```bash
yeedu metastore-catalog list-linked-tenant-secrets -h
```
```bash
usage:  list-linked-tenant-secrets [-h]
                                   [--metastore_catalog_secret_tenant_id METASTORE_CATALOG_SECRET_TENANT_ID]
                                   [--catalog_type {DATABRICKS UNITY,HIVE,AWS GLUE}]
                                   [--metastore_catalog_id METASTORE_CATALOG_ID]
                                   [--limit LIMIT] [--page_number PAGE_NUMBER]
                                   [--json-output [{pretty,default}]]
                                   [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_secret_tenant_id METASTORE_CATALOG_SECRET_TENANT_ID
                        ID of the metastore catalog for which the tenant secrets
                        should be listed.
  --catalog_type {DATABRICKS UNITY,HIVE,AWS GLUE}
                        Specify the type of catalog being configured.
  --metastore_catalog_id METASTORE_CATALOG_ID
                        ID of the metastore catalog for which the tenant secrets
                        should be listed.
  --limit LIMIT         Provide limit to list number of tenant secrets. (default:
                        10)
  --page_number PAGE_NUMBER
                        Page number for pagination. (default: 1)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)

```
- Example:
```bash
yeedu metastore-catalog  list-linked-tenant-secrets
```
- Console Output:
```json
{
  "data": [
    {
      "metastore_catalog_secret_tenant_id": 6,
      "metastore_catalog": {
        "metastore_catalog_id": 13,
        "name": "hive-3",
        "description": null,
        "catalog_type": "HIVE"
      },
      "metastore_details": {
        "hive_catalog_populated_keys": [
          "HIVE-SITE.XML",
          "CORE-SITE.XML",
          "HDFS-SITE.XML"
        ]
      },
      "metastore_secrets_tenant": {
        "secrets_tenant_id": 6,
        "name": "test_new_form_tenant_hive",
        "description": null,
        "secret_type": "HIVE BASIC"
      },
      "object_storage_secrets_tenant": {
        "secrets_tenant_id": 1,
        "name": "aws_secret",
        "description": "AWS credentials for accessing S3",
        "secret_type": "AWS ACCESS SECRET KEY PAIR"
      },
      "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
      "created_by": {
        "user_id": 6,
        "username": "yeedu@yeedu.com"
      },
      "modified_by": {
        "user_id": 4,
        "username": "yeedu@yeedu.com"
      },
      "last_update_date": "2025-04-09T03:51:24.692163+00:00",
      "from_date": "2025-02-21T09:08:46.557403+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 10
  }
}

```

### List Workspace Associated Secrets
```bash
yeedu metastore-catalog list-linked-workspace-secrets -h
```
```bash
usage:  list-linked-workspace-secrets [-h] [--workspace_id WORKSPACE_ID]
                                      [--catalog_type {DATABRICKS UNITY,HIVE,AWS GLUE}]
                                      [--metastore_catalog_secret_workspace_id METASTORE_CATALOG_SECRET_WORKSPACE_ID]
                                      [--metastore_catalog_id METASTORE_CATALOG_ID]
                                      [--limit LIMIT] [--page_number PAGE_NUMBER]
                                      [--json-output [{pretty,default}]]
                                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        ID of the workspace.
  --catalog_type {DATABRICKS UNITY,HIVE,AWS GLUE}
                        Specify the type of catalog being configured.
  --metastore_catalog_secret_workspace_id METASTORE_CATALOG_SECRET_WORKSPACE_ID
                        Secret mapping ID.
  --metastore_catalog_id METASTORE_CATALOG_ID
                        Catalog ID.
  --limit LIMIT         Limit for pagination. (default: 10)
  --page_number PAGE_NUMBER
                        Page number for pagination. (default: 1)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```
- Example:
```bash
 yeedu metastore-catalog list-linked-workspace-secrets  --workspace_id 4

```
- Console Output:
```json
{
  "data": [
    {
      "metastore_catalog_secret_workspace_id": 2,
      "metastore_catalog": {
        "metastore_catalog_id": 13,
        "name": "hive-3",
        "description": null,
        "catalog_type": "HIVE"
      },
      "metastore_secrets_workspace": {
        "secrets_workspace_id": 13,
        "name": "test_hive_workpce_41",
        "description": "hive_41",
        "secret_type": "HIVE BASIC"
      },
      "object_storage_secrets_workspace": {
        "secrets_workspace_id": 9,
        "name": "aws_secret_33",
        "description": "AWS credentials for accessing S3",
        "secret_type": "AWS ACCESS SECRET KEY PAIR"
      },
      "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
      "created_by": {
        "user_id": 20,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 20,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2025-04-14T08:05:51.438399+00:00",
      "from_date": "2025-04-14T08:05:51.438399+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 10
  }
}

```

### List User Associated Secrets
```bash
yeedu metastore-catalog list-linked-user-secrets -h
```
```bash
sage:  list-linked-user-secrets [-h] [--user_id USER_ID]
                                 [--catalog_type {DATABRICKS UNITY,HIVE,AWS GLUE}]
                                 [--metastore_catalog_secret_user_id METASTORE_CATALOG_SECRET_USER_ID]
                                 [--metastore_catalog_id METASTORE_CATALOG_ID]
                                 [--limit LIMIT] [--page_number PAGE_NUMBER]
                                 [--json-output [{pretty,default}]]
                                 [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --user_id USER_ID     User ID associated with the linked secrets.
  --catalog_type {DATABRICKS UNITY,HIVE,AWS GLUE}
                        Specify the type of catalog being configured.
  --metastore_catalog_secret_user_id METASTORE_CATALOG_SECRET_USER_ID
                        Metastore catalog secret user ID.
  --metastore_catalog_id METASTORE_CATALOG_ID
                        ID of the metastore catalog.
  --limit LIMIT         Limit number of results. (default: 10)
  --page_number PAGE_NUMBER
                        Page number for pagination. (default: 1)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'.
                        (default: false)
```
- Example:
```bash
yeedu metastore-catalog list-linked-user-secrets
```
- Console Output:
```json
{
  "data": [
    {
      "metastore_catalog_secret_user_id": 3,
      "metastore_catalog": {
        "metastore_catalog_id": 13,
        "name": "hive-3",
        "description": null,
        "catalog_type": "HIVE"
      },
      "metastore_secrets_user": {
        "secrets_user_id": 36,
        "name": "sahith_secret",
        "description": "cli secret user",
        "secret_type": "HIVE BASIC"
      },
      "object_storage_secrets_user": {
        "secrets_user_id": 38,
        "name": "aws_secret_user",
        "description": "AWS credentials for accessing S3",
        "secret_type": "AWS ACCESS SECRET KEY PAIR"
      },
      "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
      "created_by": {
        "user_id": 20,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 20,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2025-04-14T08:11:20.555936+00:00",
      "from_date": "2025-04-14T08:11:20.555936+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 10
  }
}
```

---

## Catalog Operations

| Command Name                     | Utility                                                   |
|----------------------------------|------------------------------------------------------------|
| [list](#list-metastore-catalogs)       | To list all metastore catalogs.                            |
| [search](#search-metastore-catalogs)   | To search metastore catalogs by name or type.              |

### List Metastore Catalog
```bash
yeedu metastore-catalog list -h
```
```bash
usage:  list [-h] [--catalog_type {DATABRICKS UNITY,HIVE}]
             [--metastore_catalog_id METASTORE_CATALOG_ID] [--limit LIMIT]
             [--page_number PAGE_NUMBER] [--json-output [{pretty,default}]]
             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --catalog_type {DATABRICKS UNITY,HIVE}
                        Filter results by catalog type
  --metastore_catalog_id METASTORE_CATALOG_ID
                        Filter by specific metastore catalog ID
  --limit LIMIT         Number of records to return (default: 100)
  --page_number PAGE_NUMBER
                        Page number for pagination (default: 1)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the output in YAML format if set to true.
                        (default: false)

```
- Example: 
```bash
  yeedu metastore-catalog list 
```
- Console Output:
```json
{
  "data": [
    {
      "metastore_catalog_id": 24,
      "name": "unity_cli",
      "description": "unity from cli",
      "catalog_type": "DATABRICKS UNITY",
      "metastore_details": {
        "endpoint": "https://adb-1234567890123456.7.azuredatabricks.net",
        "default_catalog": "default_catalog",
        "storage_path": "s3a://test/test"
      },
      "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
      "created_by": {
        "user_id": 20,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 24,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2025-04-11T05:18:49.220859+00:00",
      "from_date": "2025-04-11T05:19:11.533688+00:00",
      "to_date": "infinity"
    },
    {
      "metastore_catalog_id": 17,
      "name": "hive_cli",
      "description": "hive from cli",
      "catalog_type": "HIVE",
      "metastore_details": {
        "hive_metastore_populated_keys": [
          "HIVE-SITE.XML"
        ]
      },
      "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
      "created_by": {
        "user_id": 20,
        "username": "ysu0000@yeedu.io"
      },
      "modified_by": {
        "user_id": 17,
        "username": "ysu0000@yeedu.io"
      },
      "last_update_date": "2025-04-10T10:49:34.8833+00:00",
      "from_date": "2025-04-10T10:49:34.8833+00:00",
      "to_date": "infinity"
    },
  ]
}
```
### Search Metastore Catalog
```bash
yeedu metastore-catalog search -h
```
```bash
usage:  search [-h] --metastore_catalog_name METASTORE_CATALOG_NAME
               [--catalog_type {DATABRICKS UNITY,HIVE}] [--limit LIMIT]
               [--page_number PAGE_NUMBER] [--json-output [{pretty,default}]]
               [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_name METASTORE_CATALOG_NAME
                        Filter by catalog name
  --catalog_type {DATABRICKS UNITY,HIVE}
                        Filter results by catalog type
  --limit LIMIT         Number of records to return (default: 100)
  --page_number PAGE_NUMBER
                        Page number for pagination (default: 1)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the output in YAML format if set to true.
                        (default: false)

```
- Example:
```bash
yeedu metastore-catalog search --metastore_catalog_name='hive_test'

```
- console output:
```json
{
  "data": [
    {
      "metastore_catalog_id": 9,
      "name": "hive_test_789",
      "description": null,
      "catalog_type": "HIVE",
      "metastore_details": {
        "hive_metastore_populated_keys": [
          "HIVE-SITE.XML",
          "HDFS-SITE.XML",
          "KRB5.CONF"
        ]
      },
      "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
      "created_by": {
        "user_id": 4,
        "username": "yeedu@yeedu.com"
      },
      "modified_by": {
        "user_id": 9,
        "username": "yeedu@yeedu.com"
      },
      "last_update_date": "2025-04-09T03:51:24.692163+00:00",
      "from_date": "2025-02-24T06:27:58.586233+00:00",
      "to_date": "infinity"
    },
    {
      "metastore_catalog_id": 3,
      "name": "hive_test",
      "description": null,
      "catalog_type": "HIVE",
      "metastore_details": {
        "hive_metastore_populated_keys": [
          "CORE-SITE.XML",
          "HDFS-SITE.XML",
          "KRB5.CONF"
        ]
      },
      "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
      "created_by": {
        "user_id": 4,
        "username": "yeedu@yeedu.com"
      },
      "modified_by": {
        "user_id": 3,
        "username": "yeedu@yeedu.com"
      },
      "last_update_date": "2025-04-09T03:51:24.692163+00:00",
      "from_date": "2025-02-18T09:41:35.486077+00:00",
      "to_date": "infinity"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 2,
    "total_pages": 1,
    "limit": 100
  }
}
```

### Hive
| Command Name         | Utility                                        |
|----------------------|-------------------------------------------------|
| [create](#hive-create) | Create a new Hive metastore catalog.         |
| [edit](#hive-edit)     | Edit an existing Hive metastore catalog.     |
| [delete](#hive-delete) | Delete a Hive metastore catalog.             |


### Create Hive Catalog
```bash
yeedu metastore-catalog hive create -h
```
```bash
usage:  hive [-h] {create,edit,delete} ...

positional arguments:
  {create,edit,delete}
    create              Create a new Hive metastore catalog
    edit                Edit an existing Hive metastore catalog
    delete              Delete a hive metastore catalog

options:
  -h, --help            show this help message and exit

```
- Example:
```bash
 yeedu metastore-catalog hive create --name="hive_cli_test" --description="create hive metastore catalog from cli" --hive_site_xml_file_path="hive-site.xml
```
- Console Output:
```json
{
  "metastore_catalog_id": "26",
  "name": "hive_cli_test",
  "description": "create hive metastore catalog from cli",
  "catalog_type": 1,
  "metastore_hive_catalog": {
    "metastore_hive_catalog_id": "16",
    "metastore_secrets_tenant_id": null,
    "object_storage_secrets_tenant_id": null
  },
  "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
  "created_by_user_id": "20",
  "modified_by_user_id": "20",
  "last_update_date": "2025-04-14T07:04:04.412Z",
  "from_date": "2025-04-14T07:04:04.412Z",
  "to_date": null
}
```

### Edit Hive Catalog
```bash
yeedu metastore-catalog hive edit -h
```
```bash
usage: hive edit [-h] --metastore_catalog_id METASTORE_CATALOG_ID [--name NAME] [--description DESCRIPTION] [--hive_site_xml_file_path HIVE_SITE_XML_FILE_PATH]
                 [--core_site_xml_file_path CORE_SITE_XML_FILE_PATH] [--hdfs_site_xml_file_path HDFS_SITE_XML_FILE_PATH] [--krb5_conf_file_path KRB5_CONF_FILE_PATH]
                 [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        ID of the catalog to edit
  --name NAME           Specify the name of the Hive metastore catalog.
  --description DESCRIPTION
                        Specify the description of the hive metastore catalog.
  --hive_site_xml_file_path HIVE_SITE_XML_FILE_PATH
                        Specify the HIVE-SITE.xml.
  --core_site_xml_file_path CORE_SITE_XML_FILE_PATH
                        Specify the CORE-SITE.xml
  --hdfs_site_xml_file_path HDFS_SITE_XML_FILE_PATH
                        Specify the HDFS-SITE.xml
  --krb5_conf_file_path KRB5_CONF_FILE_PATH
                        Specify the krb5_conf_file_path
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```
- Example:
```bash
yeedu metastore-catalog hive edit --metastore_catalog_id=26 --name="hive_cli_test_update" --description="update hive metastore catalog from cli"
```
- Console Output:
```json
{
  "metastore_catalog_id": "26",
  "name": "hive_cli_test_update",
  "description": "update hive metastore catalog from cli",
  "catalog_type": "HIVE",
  "metastore_details": {},
  "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
  "created_by_user_id": "20",
  "modified_by_user_id": "20",
  "last_update_date": "2025-04-14T07:05:25.173Z",
  "from_date": "2025-04-14T07:04:04.412Z",
  "to_date": null
}

```

### Delete Hive Catalog
```bash
yeedu metastore-catalog hive delete -h
```
```bash
usage: hive delete [-h] --metastore_catalog_id METASTORE_CATALOG_ID [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        ID of the Hive metastore catalog to delete
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the output in YAML format if set to true. (default: false)
```
- Example:
```bash
yeedu metastore-catalog hive delete --metastore_catalog_id 26
```
- Console Output:
```json
{
  "message": "Deleted Hive Metastore Catalog Id: 26"
}

```
### Databricks Unity
| Command Name                  | Utility                                                   |
|-------------------------------|------------------------------------------------------------|
| [create](#databricks-unity-create) | Create a new Databricks Unity metastore catalog.           |
| [edit](#databricks-unity-edit)     | Edit an existing Databricks Unity metastore catalog.       |
| [delete](#databricks-unity-delete) | Delete a Databricks Unity metastore catalog. |

### Create Databricks Unity Catalog
```bash
yeedu metastore-catalog databricks-unity create -h
```
```bash
usage: databricks-unity create [-h] --name NAME --description DESCRIPTION --endpoint ENDPOINT --default_catalog DEFAULT_CATALOG --additional_catalogs ADDITIONAL_CATALOGS  --storage_path STORAGE_PATH
                               [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name NAME           Specify the name of the databricks unity metastore catalog.
  --description DESCRIPTION
                        Specify the description of the databricks unity metastore catalog.
  --endpoint ENDPOINT   Specify the Databricks endpoint URL.
  --default_catalog DEFAULT_CATALOG
                        Specify the default catalog name.
  --additional_catalogs ADDITIONAL_CATALOGS
                        Specify the catalog names to associate with this metastore in addition to the default.
  --storage_path STORAGE_PATH
                        Specify the storage path (e.g., S3 or ADLS).
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)

```
- Example:
```bash
yeedu metastore-catalog databricks-unity create --name="unity_cli_test" --description="Create unity metastore catalog from cli" --endpoint="https://adb-1234567890123456.7.azuredatabricks.net" --default_catalog="test" --additional_catalog="dev,bronze" --storage_path="s3a://my-bucket/logs/file.txt"
```
- Console Output:
```json
{
  "metastore_catalog_id": "31",
  "name": "unity_cli_test",
  "description": "Create unity metastore catalog from cli",
  "catalog_type": "DATABRICKS UNITY",
  "metastore_unity_catalog": {
    "metastore_unity_catalog_id": "7",
    "endpoint": "https://adb-1234567890123456.7.azuredatabricks.net",
    "default_catalog": "test",
    "storage_path": "s3a://my-bucket/logs/file.txt"
  },
  "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
  "created_by_user_id": "20",
  "modified_by_user_id": "20",
  "last_update_date": "2025-04-14T07:13:43.073Z",
  "from_date": "2025-04-14T07:13:43.073Z",
  "to_date": null
}

```

### Edit Databricks Unity Catalog
```bash
yeedu metastore-catalog databricks-unity edit -h
```
```bash
usage: databricks-unity edit [-h] [--metastore_catalog_id METASTORE_CATALOG_ID] [--name NAME] [--description DESCRIPTION] [--endpoint ENDPOINT] [--default_catalog DEFAULT_CATALOG] [--additional_catalogs ADDITIONAL_CATALOGS]
                             [--storage_path STORAGE_PATH] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        ID of the catalog to edit
  --name NAME           Specify the name of the databricks unity metastore catalog.
  --description DESCRIPTION
                        Specify the description of the databricks unity metastore catalog.
  --endpoint ENDPOINT   Specify the Databricks endpoint URL.
  --default_catalog DEFAULT_CATALOG
                        Specify the default catalog name.
  --additional_catalogs ADDITIONAL_CATALOGS
                        Specify the catalog names to associate with this metastore in addition to the default.
  --storage_path STORAGE_PATH
                        Specify the storage path (e.g., S3 or ADLS).
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)

```
- Example:
```bash
yeedu metastore-catalog databricks-unity edit --metastore_catalog_id 31 --name="unity_cli_test_updated" --description="update unity metastore catalog from cli"
```
- Console Output:
```json
{
  "metastore_catalog_id": "31",
  "name": "unity_cli_test_updated",
  "description": "update unity metastore catalog from cli",
  "catalog_type": "DATABRICKS UNITY",
  "metastore_details": {},
  "tenant_id": "234e28f0-c93f-4b27-b5b0-83c4e4b1dae2",
  "created_by_user_id": "20",
  "modified_by_user_id": "20",
  "last_update_date": "2025-04-14T07:14:58.447Z",
  "from_date": "2025-04-14T07:13:43.073Z",
  "to_date": null
}
```

### Delete Databricks Unity Catalog
```bash
yeedu metastore-catalog databricks-unity delete -h
```
```bash
usage: databricks-unity delete [-h] --metastore_catalog_id METASTORE_CATALOG_ID [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        ID of the databricks unity metastore catalog to delete
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the output in YAML format if set to true. (default: false)

```
- Example:
```bash
yeedu metastore-catalog databricks-unity delete --metastore_catalog_id 31
```
- Console Output:
```json
{
  "message": "Deleted Metastore Unity Catalog: 31"
}
```


### Glue Catalog
| Command Name             | Utility                                                  |
|--------------------------|----------------------------------------------------------|
| [create](#glue-catalog-create) | Create a new Glue metastore catalog.                      |
| [edit](#glue-catalog-edit)     | Edit an existing Glue metastore catalog.                  |
| [delete](#glue-catalog-delete) | Delete a Glue metastore catalog.                          |

### Create AWS Glue Catalog
```bash
yeedu metastore-catalog aws-glue create -h
```
```bash
usage: aws-glue create [-h] --name NAME [--description DESCRIPTION] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --name NAME           Specify the name of the Glue metastore catalog.
  --description DESCRIPTION
                        Specify the description of the Glue metastore catalog.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```
- Example:
```bash
yeedu metastore-catalog aws-glue create --name "glue_catalog_2" --description "description for catalog"
```
- Console Output:
```json
{
  "metastore_catalog_id": "25",
  "name": "glue_catalog_2",
  "description": "description for catalog",
  "catalog_type": 3,
  "metastore_details": {
    "metastore_glue_catalog_id": "5"
  },
  "tenant_id": "d156ae4c-13b2-40d5-9f61-dd9c81550747",
  "created_by_user_id": "2",
  "modified_by_user_id": "2",
  "last_update_date": "2025-09-16T08:34:11.782Z",
  "from_date": "2025-09-16T08:34:11.782Z",
  "to_date": null
}
```

### Edit AWS Glue Catalog
```bash
yeedu metastore-catalog aws-glue edit -h
```
```bash
usage: aws-glue edit [-h] --metastore_catalog_id METASTORE_CATALOG_ID [--name NAME] [--description DESCRIPTION] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        ID of the catalog to edit
  --name NAME           Specify the name of the Glue metastore catalog.
  --description DESCRIPTION
                        Specify the description of the Glue metastore catalog.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```
- Example:
```bash
yeedu metastore-catalog aws-glue edit --metastore_catalog_id 25 --name "glue_2"
```
- Console Output:
```json
{
  "metastore_catalog_id": "25",
  "name": "glue_2",
  "description": "description for catalog",
  "catalog_type": "AWS GLUE",
  "metastore_details": {},
  "tenant_id": "d156ae4c-13b2-40d5-9f61-dd9c81550747",
  "created_by_user_id": "2",
  "modified_by_user_id": "2",
  "last_update_date": "2025-09-16T08:35:22.150Z",
  "from_date": "2025-09-16T08:34:11.782Z",
  "to_date": null
}
```

### Delete AWS Glue Catalog
```bash
yeedu metastore-catalog aws-glue delete -h
```
```bash
usage: aws-glue delete [-h] --metastore_catalog_id METASTORE_CATALOG_ID [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        ID of the Glue metastore catalog to delete
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the output in YAML format if set to true. (default: false)
```
- Example:
```bash
yeedu metastore-catalog aws-glue delete --metastore_catalog_id 25
```
- Console Output:
```json
{
  "message": "Deleted Glue Metastore Catalog Id: 25"
}
```

### Catalog Explorer
| Command Name                                  | Utility                                          |
| --------------------------------------------- | ------------------------------------------------ |
| [list-catalogs](#list-catalogs)               | List catalogs for a metastore.                   |
| [list-schemas](#list-schemas)                 | List schemas for a given catalog in a metastore. |
| [list-tables](#list-tables)                   | List tables for a schema in a metastore.         |
| [list-columns](#list-columns)                 | List columns for a table in a metastore.         |
| [list-table-summaries](#list-table-summaries) | List table summaries for a metastore.            |
| [get-table-ddl](#get-table-ddl)               | Retrieve DDL for a table in a metastore.         |
| [list-functions](#list-functions)             | List functions for a schema in a metastore.      |
| [list-volumes](#list-volumes)                 | List volumes for a schema in a metastore.        |

### list-catalogs

```bash
yeedu catalog-explorer list-catalogs -h
```

```bash
usage:  list-catalogs [-h] --metastore_catalog_id METASTORE_CATALOG_ID --workspace_id WORKSPACE_ID 
                          [--json-output [{pretty,default}]] 
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        To list catalogs of a specific metastore
  --workspace_id WORKSPACE_ID
                        To list catalogs of a metastore using the secrets of sepcific workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-catalogs example with all the required arguments passed.

```bash
yeedu catalog-explorer list-catalogs --metastore_catalog_id 32 --workspace_id 1
```

- Console output

```bash
[
  {
    "name": "catalog_name",
    "owner": "user@example.com",
    "storage_root": "s3://example-bucket/path/to/root",
    "storage_location": "s3://example-bucket/path/to/catalog/location",
    "full_name": "catalog_name",
    "created_at": 1746006869220,
    "updated_at": 1746006869220,
    "updated_by": "user@example.com",
    "type": "CATALOG"
  }
]
```

### list-schemas

```bash
yeedu catalog-explorer list-schemas -h
```

```bash
usage:  list-schemas [-h] --metastore_catalog_id METASTORE_CATALOG_ID 
                          --workspace_id WORKSPACE_ID 
                          [--catalog_name CATALOG_NAME] 
                          [--json-output [{pretty,default}]] 
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        To list schemas of for specific metastore
  --workspace_id WORKSPACE_ID
                        To list schemas of a metastore using the secrets of sepcific workspace.
  --catalog_name CATALOG_NAME
                        To list schemas for a specific catalog.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-schemas example with all the required arguments passed.

```bash
yeedu catalog-explorer list-schemas --metastore_catalog_id 32 --workspace_id 1 --catalog_name="bronze"
```

- Console output

```bash
[
  {
    "name": "default",
    "catalog_name": "bronze",
    "owner": "user@example.com",
    "comment": "Default schema (auto-created)",
    "full_name": "bronze.default",
    "created_at": 1742996088010,
    "created_by": "user@example.com",
    "updated_at": 1742996088010,
    "updated_by": "user@example.com",
    "type": "SCHEMA"
  }
]
```


### list-tables

```bash
yeedu catalog-explorer list-tables -h
```

```bash
usage:  list-tables [-h] --metastore_catalog_id METASTORE_CATALOG_ID 
                         --workspace_id WORKSPACE_ID [--catalog_name CATALOG_NAME] 
                         --schema_name SCHEMA_NAME 
                         [--json-output [{pretty,default}]]
                         [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        To list tables of for specific metastore
  --workspace_id WORKSPACE_ID
                        To list tables of a metastore using the secrets of sepcific workspace.
  --catalog_name CATALOG_NAME
                        To list tables for a specific catalog.
  --schema_name SCHEMA_NAME
                        To list tables for a specific schema.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-tables example with all the required arguments passed.

```bash
yeedu catalog-explorer list-tables --metastore_catalog_id 21 --workspace_id 1 --catalog_name="bronze" --schema_name="information_schema"
```

- Console output

```bash
[
  {
    "name": "tables",
    "catalog_name": "bronze",
    "schema_name": "information_schema",
    "owner": "System user",
    "full_name": "bronze.information_schema.tables",
    "created_at": 1742996088198,
    "created_by": "System user",
    "updated_at": 1742996088198,
    "updated_by": "System user",
    "type": "TABLE"
  }
]
```

### list-columns

```bash
yeedu catalog-explorer list-columns -h
```

```bash
usage:  list-columns [-h] --metastore_catalog_id METASTORE_CATALOG_ID 
                          --workspace_id WORKSPACE_ID 
                          [--catalog_name CATALOG_NAME] 
                          --schema_name SCHEMA_NAME --table_name TABLE_NAME
                          [--json-output [{pretty,default}]] 
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        To list columns of table for specific metastore
  --workspace_id WORKSPACE_ID
                        To list columns of a table of using the secrets of sepcific workspace.
  --catalog_name CATALOG_NAME
                        To list columns of a tables for a specific catalog.
  --schema_name SCHEMA_NAME
                        To list columns of a table for a specific schema.
  --table_name TABLE_NAME
                        To list columns for a specific table.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-columns example with all the required arguments passed.

```bash
yeedu catalog-explorer list-columns --metastore_catalog_id 21 --workspace_id 1 --catalog_name="bronze" --schema_name="default" --table_name="sales"
```

- Console output

```bash
[
  {
    "name": "grantor",
    "type_text": "string",
    "type_name": "STRING",
    "position": 0,
    "type": "INT"
  }
]
```

### list-table-summaries

```bash
yeedu catalog-explorer list-table-summaries -h
```

```bash
usage:  list-table-summaries [-h] --metastore_catalog_id METASTORE_CATALOG_ID 
                                  --workspace_id WORKSPACE_ID 
                                  [--catalog_name CATALOG_NAME] 
                                  [--cached_tables CACHED_TABLES] 
                                  [--json-output [{pretty,default}]]
                                  [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        To list table summaries for specific metastore
  --workspace_id WORKSPACE_ID
                        To list table summaries by using the secrets of sepcific workspace.
  --catalog_name CATALOG_NAME
                        To list columns of a tables for a specific catalog.
  --cached_tables CACHED_TABLES
                        To list columns of a table for a specific schema.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-table-summaries example

```bash
yeedu catalog-explorer list-table-summaries --metastore_catalog_id 21 --workspace_id 1 --catalog_name="bronze"
```

- Console output

```bash
[
  "bronze.information_schema.tables"
]
```

### get-table-ddl

```bash
yeedu catalog-explorer get-table-ddl -h
```

```bash
usage:  get-table-ddl [-h] --metastore_catalog_id METASTORE_CATALOG_ID 
                           --workspace_id WORKSPACE_ID 
                           [--cached_tables CACHED_TABLES] 
                           [--json-output [{pretty,default}]] 
                           [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        To list table summaries for specific metastore
  --workspace_id WORKSPACE_ID
                        To list table ddl of a metastore of sepcific workspace.
  --cached_tables CACHED_TABLES
                        To list table ddl for a table.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- get-table-ddl example with all the required arguments passed.

```bash
yeedu catalog-explorer get-table-ddl --metastore_catalog_id 21 --workspace_id 1 --cached_tables="test"
```

- Console output

```bash
[
  {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  }
]
```

### list-functions

```bash
yeedu catalog-explorer list-functions -h
```

```bash
usage:  list-functions [-h] --metastore_catalog_id METASTORE_CATALOG_ID 
                            --workspace_id WORKSPACE_ID 
                            [--catalog_name CATALOG_NAME] 
                            [--schema_name SCHEMA_NAME] 
                            [--json-output [{pretty,default}]]
                            [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        The ID of the Metastore Catalog to retrieve functions from.
  --workspace_id WORKSPACE_ID
                        The ID of the workspace to retrieve functions for.
  --catalog_name CATALOG_NAME
                        The name of the catalog to retrieve functions from.
  --schema_name SCHEMA_NAME
                        The name of the schema to retrieve functions from.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-functions example with all the required arguments passed.

```bash
yeedu catalog-explorer list-functions --metastore_catalog_id 21 --workspace_id 1 --catalog_name="sample_catalog" --schema_name="default_schema"
```

- Console output

```bash

  {
    "name": "my_function",
    "catalog_name": "sample_catalog",
    "schema_name": "default_schema",
    "data_type": "STRING",
    "full_data_type": "STRING",
    "routine_body": "SQL",
    "routine_definition": "CONCAT(first_name, ' ', last_name)",
    "parameter_style": "S",
    "is_deterministic": true,
    "sql_data_access": "CONTAINS_SQL",
    "security_type": "DEFINER",
    "specific_name": "my_function",
    "owner": "owner@example.com",
    "properties": "{\"sqlConfig.spark.sql.ansi.enabled\":\"true\",\"sqlConfig.spark.sql.sources.default\":\"delta\"}\n",
    "metastore_id": "24820380-2435-3444-6567-5893393",
    "full_name": "sample_catalog.default_schema.my_function",
    "created_at": 1700000000000,
    "created_by": "creator@example.com",
    "updated_at": 1700000500000,
    "updated_by": "updater@example.com",
    "function_id": "6838900-79004-8568-9099-235512",
    "securable_type": "FUNCTION",
    "securable_kind": "FUNCTION_STANDARD",
    "icon_type": "FUNCTION"
  }
]
```


### list-volumes

```bash
yeedu catalog-explorer list-volumes -h
```

```bash
usage:  list-volumes [-h] --metastore_catalog_id METASTORE_CATALOG_ID 
                          --workspace_id WORKSPACE_ID 
                          [--catalog_name CATALOG_NAME] 
                          [--schema_name SCHEMA_NAME] 
                          [--json-output [{pretty,default}]]
                          [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --metastore_catalog_id METASTORE_CATALOG_ID
                        The ID of the Metastore Catalog to retrieve volumes from.
  --workspace_id WORKSPACE_ID
                        The ID of the workspace to retrieve volumes for.
  --catalog_name CATALOG_NAME
                        The name of the catalog to retrieve volumes from.
  --schema_name SCHEMA_NAME
                        The name of the schema to retrieve volumes from.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- list-volumes example with all the required arguments passed.

```bash
yeedu catalog-explorer list-volumes --metastore_catalog_id 21 --workspace_id 1 --catalog_name="enterprise_catalog" --schema_name="finance_schema"
```

- Console output

```bash
[
  {
    "name": "sales_data_volume",
    "catalog_name": "enterprise_catalog",
    "schema_name": "finance_schema",
    "resource_name": "/metastores/13b97132-f334-405b-ad70-0a1e4a20d587/volumes/5202395f-24aa-4eb0-ab12-02158edbfe6a",
    "volume_type": "MANAGED",
    "storage_location": "abfss://databricks-metastore@corpdatabricks.dfs.core.windows.net/metastore/13b97132-f334-405b-ad70-0a1e4a20d587/volumes/5202395f-24aa-4eb0-ab12-02158edbfe6a",
    "owner": "data.engineer@company.com",
    "comment": "Volume storing quarterly sales data in Parquet format",
    "full_name": "enterprise_catalog.finance_schema.sales_data_volume",
    "volume_id": "5202395f-24aa-4eb0-ab12-02158edbfe6a",
    "metastore_id": "13b97132-f334-405b-ad70-0a1e4a20d587",
    "created_at": 1734086400000,
    "created_by": "data.engineer@company.com",
    "updated_at": 1734172800000,
    "updated_by": "lead.dataops@company.com",
    "securable_type": "VOLUME",
    "securable_kind": "VOLUME_STANDARD",
    "schema_id": "a81f1e1a-2bf3-4dd0-8afe-96fa5da49981",
    "catalog_id": "e4b7735d-fc8c-4716-903a-d6896474b355",
    "icon_type": "VOLUME"
  }
]
```


# Git Credentials

| Command Name                      | Utility                                                  |
| --------------------------------- | -------------------------------------------------------- |
| [create](#create-git-credential)  | Add a new Git credential for authentication.             |
| [list](#list-git-credentials)     | List stored Git credentials of specified git provider.   |
| [get](#get-git-credential)        | Retrieve details of a specific credential.               |
| [edit](#edit-git-credential)      | Modify an existing Git credential.                       |
| [delete](#delete-git-credential)  | Remove an existing Git credential.                       |

### create

```bash
yeedu git-credentials create -h
```

```bash
usage:  create [-h] --git_provider {GitHub,BitBucket Cloud,GitLab,Azure DevOps Services,GitHub Enterprise Server,BitBucket Server,GitLab Enterprise Edition,AWS CodeCommit} --username USERNAME --token TOKEN
               [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --git_provider {GitHub,BitBucket Cloud,GitLab,Azure DevOps Services,GitHub Enterprise Server,BitBucket Server,GitLab Enterprise Edition,AWS CodeCommit}
                        Specifies the Git provider (e.g., GitHub, GitLab, Bitbucket, Azure DevOps).
  --username USERNAME   The username or email associated with the Git provider account.
  --token TOKEN         The credential used to authenticate with the Git provider (e.g., Personal Access Token, App Password, IAM Git password).
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git-credentials create --git_provider="GIT_HUB" --username="user123" --token="ghp_abcd1234567890"
```

- Console output:

```bash
{
  "git_credential_id": "3",
  "git_username": "user123",
  "lookup_git_providers_id": "1",
  "tenant_id": "39262fc1-e77b-420b-83e6-952c5bca2857",
  "created_by_user_id": "48",
  "modified_by_user_id": "48",
  "last_update_date": "2025-05-29T11:07:21.218Z",
  "from_date": "2025-05-29T11:07:21.218Z",
  "to_date": null
}
```


### list

```bash
yeedu git-credentials list -h
```

```bash
usage:  list [-h] --git_provider {GitHub,BitBucket Cloud,GitLab,Azure DevOps Services,GitHub Enterprise Server,BitBucket Server,GitLab Enterprise Edition,AWS CodeCommit} [--json-output [{pretty,default}]]
             [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --git_provider {GitHub,BitBucket Cloud,GitLab,Azure DevOps Services,GitHub Enterprise Server,BitBucket Server,GitLab Enterprise Edition,AWS CodeCommit}
                        Specify the Git provider for which credentials need to be listed (e.g., GitHub, GitLab, Bitbucket, Azure DevOps).
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git-credentials list --git_provider="GIT_HUB"
```

- Console output:

```bash
[
  {
    "git_credential_id": 3,
    "git_username": "user123",
    "lookup_git_provider": {
      "lookup_git_provider_id": 1,
      "name": "GIT_HUB",
      "description": "A cloud-based Git repository hosting service developed by GitHub, Inc., providing source code management and collaboration features."
    },
    "tenant_id": "39262fc1-e77b-420b-83e6-952c5bca2857",
    "created_by": {
      "user_id": 48,
      "username": "yeedu@yeedu.com"
    },
    "modified_by": {
      "user_id": 48,
      "username": "yeedu@yeedu.com"
    },
    "last_update_date": "2025-05-29T04:40:40.893503+00:00",
    "from_date": "2025-05-29T04:40:40.893503+00:00",
    "to_date": "infinity"
  }
]
```

### get

```bash
yeedu git-credentials get -h
```

```bash
usage:  get [-h] --git_credential_id GIT_CREDENTIAL_ID [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --git_credential_id GIT_CREDENTIAL_ID
                        Specify the Git credential ID to retrieve details.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git-credentials get --git_credential_id=3
```

- Console output:

```bash
{
  "git_credential_id": 3,
  "git_username": "user123",
  "lookup_git_provider": {
    "lookup_git_provider_id": 1,
    "name": "GIT_HUB",
    "description": "A cloud-based Git repository hosting service developed by GitHub, Inc., providing source code management and collaboration features."
  },
  "tenant_id": "39262fc1-e77b-420b-83e6-952c5bca2857",
  "created_by": {
    "user_id": 48,
    "username": "yeedu@yeedu.com"
  },
  "modified_by": {
    "user_id": 48,
    "username": "yeedu@yeedu.com"
  },
  "last_update_date": "2025-05-29T04:40:40.893503+00:00",
  "from_date": "2025-05-29T04:40:40.893503+00:00",
  "to_date": "infinity"
}
```


### edit

```bash
yeedu git-credentials edit -h
```

```bash
usage:  edit [-h] --git_credential_id GIT_CREDENTIAL_ID --username USERNAME --token TOKEN [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --git_credential_id GIT_CREDENTIAL_ID
                        Specify the Git credential ID to update.
  --username USERNAME   The updated username associated with the Git provider account.
  --token TOKEN         The updated credential (Personal Access Token, App Password, IAM Git password).
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git-credentials edit --git_credential_id=35 --username="newUser" --token="newToken123"
```

- Console output:

```bash
{
  "git_credential_id": "3",
  "git_username": "newUser",
  "lookup_git_providers_id": "1",
  "tenant_id": "39262fc1-e77b-420b-83e6-952c5bca2857",
  "created_by_user_id": "48",
  "modified_by_user_id": "48",
  "last_update_date": "2025-05-29T11:06:00.231Z",
  "from_date": "2025-05-29T04:40:40.893Z",
  "to_date": null
}
```


### delete

```bash
yeedu git-credentials delete -h
```

```bash
usage:  delete [-h] --git_credential_id GIT_CREDENTIAL_ID [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --git_credential_id GIT_CREDENTIAL_ID
                        Specify the Git credential ID to delete.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git-credentials delete --git_credential_id=3
```

- Console output:

```bash
{
  "message": "Deleted git credential id: 3."
}
```

# Git

| Command Name                       | Utility                                                                          |
| ---------------------------------- | -------------------------------------------------------------------------------- |
| [clone](#clone)                    | Clone a Git repository into the workspace.                                       |
| [list-branches](#list-branches)    | Retrieve all branches for a repository.                                          |
| [create-branch](#create-branch)    | Create a new branch within the repository.                                       |
| [switch-branch](#switch-branch)    | Switch to a different branch.                                                    |
| [status](#status)                  | Check the Git status of files.                                                   |
| [stage](#stage)                    | Stage files for commit.                                                          |
| [file-diff](#file-diff)            | Difference between the current modified changes and the last previous commit.    |
| [commit-push](#commit-push)        | Commit and push changes to the remote repo.                                      |
| [pull](#pull)                      | Pull the latest changes from remote.                                             |
| [clone-status](#clone-status)      | Check the status of a repository clone.                                          |
| [clone-log](#clone-log)            | View logs for a Git clone operation.                                             |
| [clone-errors](#clone-errors)      | Retrieve errors related to cloning.                                              |
| [discard](#discard)                | Discard local changes.                                                           |


### clone

```bash
yeedu git clone -h
```

```bash
usage:  clone [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] [--file_id FILE_ID] [--file_path FILE_PATH] --git_url GIT_URL --git_provider
              {GitHub,BitBucket Cloud,GitLab,Azure DevOps Services,GitHub Enterprise Server,BitBucket Server,GitLab Enterprise Edition,AWS CodeCommit} --git_branch GIT_BRANCH [--git_folder_name GIT_FOLDER_NAME]
              [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID where the Git repo should be cloned.
  --workspace_name WORKSPACE_NAME
                        Workspace name as an alternative to workspace_id.
  --file_id FILE_ID     Workspace file ID used to determine where the Git repo will be cloned.
  --file_path FILE_PATH
                        Workspace file path where the Git repo will be cloned.
  --git_url GIT_URL     Git repository URL to be cloned (e.g., https://github.com/org/repo.git).
  --git_provider {GitHub,BitBucket Cloud,GitLab,Azure DevOps Services,GitHub Enterprise Server,BitBucket Server,GitLab Enterprise Edition,AWS CodeCommit}
                        Specifies the Git provider (e.g., GitHub, GitLab, Bitbucket, Azure DevOps, etc.).
  --git_branch GIT_BRANCH
                        Branch name to clone the specific branch of the repository (e.g., 'main').
  --git_folder_name GIT_FOLDER_NAME
                        Folder name for the cloned Git repo. If not provided, the folder name will be the same as the repository name.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git clone --workspace_id=162 --file_path="/" --git_url="https://github.com/dummy/repo.git" --git_provider="GIT_HUB" --git_branch="main" --git_folder_name="project-repo-clone"
```

- Console output:

```bash
{
  "message": "Git clone repo has been initiated.",
  "workspace_file_id": 49,
  "full_file_path": "file:///files/project-repo-clone"
}
```


### list-branches

```bash
yeedu git list-branches -h
```

```bash
usage:  list-branches [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] [--file_id FILE_ID] [--file_path FILE_PATH] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID where the Git Folder is located.
  --workspace_name WORKSPACE_NAME
                        Workspace name as an alternative to workspace_id.
  --file_id FILE_ID     File ID of the Git folder within the workspace.
  --file_path FILE_PATH
                        Full file path to the Git folder within the workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git list-branches --workspace_id=162 --file_id=1
```

- Console output:

```bash
{
  "branches": [
    "main",
    "dev",
    "feature/v1.0",
    "feature/v2.0"
  ]
}
```

### create-branch

```bash
yeedu git create-branch -h
```

```bash
usage:  create-branch [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] --branch_name BRANCH_NAME [--file_id FILE_ID] [--file_path FILE_PATH] [--json-output [{pretty,default}]]
                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID used for filtering.
  --workspace_name WORKSPACE_NAME
                        Workspace name used for filtering.
  --branch_name BRANCH_NAME
                        The name of the branch that needs to be created (must follow Git naming conventions).
  --file_id FILE_ID     File ID of the Git folder within the workspace.
  --file_path FILE_PATH
                        Full file path to the Git folder within the workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git create-branch --workspace_id=123 --file_id=45 --branch_name="new-feature"
```

- Console output:

```bash
{
  "message": "A branch with name 'new-feature' has been created successfully."
}
```

### switch-branch

```bash
yeedu git switch-branch -h
```

```bash
usage:  switch-branch [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] --branch_name BRANCH_NAME [--file_id FILE_ID] [--file_path FILE_PATH] [--json-output [{pretty,default}]]
                      [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID used for filtering.
  --workspace_name WORKSPACE_NAME
                        Workspace name used for filtering.
  --branch_name BRANCH_NAME
                        The name of the Git branch to switch to (must follow Git naming conventions).
  --file_id FILE_ID     File ID of the Git folder within the workspace.
  --file_path FILE_PATH
                        Full file path to the Git folder within the workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git switch-branch --workspace_id=123 --file_id=45 --branch_name="dev"
```

- Console output:

```bash
{
  "message": "Switched to the branch 'dev'."
}
```

### status

```bash
yeedu git status -h
```

```bash
usage:  status [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] [--file_id FILE_ID] [--file_path FILE_PATH] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID where the Git Folder is located.
  --workspace_name WORKSPACE_NAME
                        Workspace name as an alternative to workspace_id.
  --file_id FILE_ID     File ID of the Git folder within the workspace.
  --file_path FILE_PATH
                        Full file path to the Git folder within the workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git status --workspace_id=123 --file_path="/reponame"
```

- Console output:

```bash
{
  "status": {
    "not_added": [
      "car.py",
      "new.py"
    ],
    "conflicted": [],
    "created": [],
    "deleted": [
      "new_file.py",
      "readme.md",
      "test.txt"
    ],
    "modified": [
      "testing/test1.py"
    ],
    "renamed": [],
    "files": [
      [
        {
          "path": "new_file.py",
          "fullFilePath": "file:///files/reponame/new_file.py",
          "index": " ",
          "working_dir": "D",
          "file_name": "new_file.py"
        },
        {
          "path": "readme.md",
          "fullFilePath": "file:///files/reponame/readme.md",
          "index": " ",
          "working_dir": "D",
          "file_name": "readme.md"
        },
        {
          "path": "test.txt",
          "fullFilePath": "file:///files/reponame/test.txt",
          "index": " ",
          "working_dir": "D",
          "file_name": "test.txt"
        },
        {
          "path": "testing/test1.py",
          "fullFilePath": "file:///files/reponame/testing/test1.py",
          "index": " ",
          "working_dir": "M",
          "file_name": "test1.py"
        },
        {
          "path": "car.py",
          "fullFilePath": "file:///files/reponame/car.py",
          "index": "?",
          "working_dir": "?",
          "file_name": "car.py"
        },
        {
          "path": "new.py",
          "fullFilePath": "file:///files/reponame/new.py",
          "index": "?",
          "working_dir": "?",
          "file_name": "new.py"
        }
      ]
    ],
    "staged": [],
    "ahead": 0,
    "behind": 0,
    "current": "main",
    "tracking": "origin/main",
    "detached": false,
    "head_commit_hash": "a72e43163713efa9760ae4cb41bc74ccb4e195e5",
    "repo_url": "https://github.com/username/reponame.git"
  }
}
```

### stage

```bash
yeedu git stage -h
```

```bash
usage:  stage [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] --file_id FILE_ID [--file_paths FILE_PATHS [FILE_PATHS ...]] [--all [{true,false}]] [--json-output [{pretty,default}]]
              [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID where the Git Folder is located.
  --workspace_name WORKSPACE_NAME
                        Workspace name as an alternative to workspace_id.
  --file_id FILE_ID     File ID of the Git folder within the workspace.
  --file_paths FILE_PATHS [FILE_PATHS ...]
                        List of full file paths to stage.
  --all [{true,false}]  If set to 'true', all files will be staged within the Git folder. (default: false)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git stage --workspace_id=123 --file_id=456 --file_paths="/reponame/file1.py,/reponame/file2.js"
```

- Console output:

```bash
{
  "message": "Files has been successfully staged."
}
```


### file-diff

```bash
yeedu git file-diff -h
```

```bash
usage:  file-diff [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] --file_id FILE_ID --file_path FILE_PATH [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID used to locate the Git folder.
  --workspace_name WORKSPACE_NAME
                        Workspace name used to locate the Git folder.
  --file_id FILE_ID     File ID of the Git folder.
  --file_path FILE_PATH
                        Full file path of the specific file to view the diff.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git file-diff --workspace_id=123 --file_id=45
```

- Console output:

```bash
{
  "diff": "diff --git a/test.py b/test.py\\nindex d8f6f5b..2601c0d 100644\\n--- a/test.py\\n+++ b/test.py\\n@@ -1,6 +1,7 @@\\n def greet_user(name):\\n     \\\"\\\"\\\"Function to greet the user.\\\"\\\"\\\"\\n-    return f\\\"Hello, {name}! Welcome to the Python world.\\\"\\n+    \\\"\\\"\\\"Lets welcome the user.\\\"\\\"\\\"\\n+    return f\\\"Hello, {name}! Welcome to the Scala world.\\\"\\n \\n def write_to_file(filename, content):\\n     \\\"\\\"\\\"Write content to a file.\\\"\\\"\\\"\\n\n"
}
```

### commit-push

```bash
yeedu git commit-push -h
```

```bash
usage:  file-diff [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] --file_id FILE_ID --file_path FILE_PATH [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID where the Git Folder is located.
  --workspace_name WORKSPACE_NAME
                        Workspace name as an alternative to workspace_id.
  --file_id FILE_ID     File ID of the Git folder within the workspace.
  --file_path FILE_PATH
                        Full file path of the specific file to view the diff.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git commit-push --workspace_id=123 --file_id=45 --file_paths="/repo/file1.py,/repo/file2.js" --commit_message="Fix issue" --description="Bug fix in authentication"
```

- Console output:

```bash
{
  "message": "Commit and push successful."
}
```


### pull

```bash
yeedu git pull -h
```

```bash
usage:  pull [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] [--file_id FILE_ID] [--file_path FILE_PATH] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID used for filtering.
  --workspace_name WORKSPACE_NAME
                        Workspace name used for filtering.
  --file_id FILE_ID     File ID of the Git folder within the workspace.
  --file_path FILE_PATH
                        Full file path to the Git folder within the workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git pull --workspace_id=123 --file_id=45
```

- Console output:

```bash
{
  "message": "Pulled the latest changes from the remote repository."
}
```


### clone-status

```bash
yeedu git clone-status -h
```

```bash
usage:  clone-status [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] [--file_id FILE_ID] [--file_path FILE_PATH] [--json-output [{pretty,default}]] [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID where the Git Folder is located.
  --workspace_name WORKSPACE_NAME
                        Workspace name as an alternative to workspace_id.
  --file_id FILE_ID     File ID of the Git folder within the workspace.
  --file_path FILE_PATH
                        Full file path to the Git folder within the workspace.
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git clone-status --workspace_id=123 --file_id=45
```

- Console output:

```bash
{
  "job_status": "COMPLETED",
  "created_by": "ysu0000@yeedu.io",
  "start_time": "2025-05-23T14:01:15.311967+05:30",
  "end_time": "infinity"
}
```

### clone-log

```bash
yeedu git clone-log -h
```

```bash
usage:  clone-log [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] [--file_id FILE_ID] [--file_path FILE_PATH] --log_type {stdout,stderr} [--json-output [{pretty,default}]]
                  [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID used to locate the Git folder.
  --workspace_name WORKSPACE_NAME
                        Workspace name used to locate the Git folder.
  --file_id FILE_ID     File ID of the Git folder within the workspace.
  --file_path FILE_PATH
                        Full file path to the Git folder within the workspace.
  --log_type {stdout,stderr}
                        Type of log to retrieve (e.g., 'error', 'info').
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git clone-log --log_type="stderr" --workspace_id=62 --file_id=714778
```

- Console output:

```bash
Cloning into 'file:///files/RepoName'...
true
```

### clone-errors

```bash
yeedu git clone-errors -h
```

```bash
usage:  clone-log [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] [--file_id FILE_ID] [--file_path FILE_PATH] --log_type {stdout,stderr} [--json-output [{pretty,default}]]
                  [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID where the Git Folder is located.
  --workspace_name WORKSPACE_NAME
                        Workspace name as an alternative to workspace_id.
  --file_id FILE_ID     File ID of the Git folder within the workspace.
  --file_path FILE_PATH
                        Full file path to the Git folder within the workspace.
  --log_type {stdout,stderr}
                        Type of log to retrieve (e.g., 'error', 'info').
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git clone-errors --workspace_id=62 --file_id=717633
```

- Console output:

```bash
{
  "data": [
    {
      "error": "OnError(Process finish with exit code 128,None,None,None,Some(org.apache.pekko.stream.connectors.amqp.impl.AmqpSourceStage$$anon$1$$anon$2$$anon$3@a03bf9e))"
    }
  ],
  "result_set": {
    "current_page": 1,
    "total_objects": 1,
    "total_pages": 1,
    "limit": 100
  }
}
```


### discard

```bash
yeedu git discard -h
```

```bash
usage:  discard [-h] [--workspace_id WORKSPACE_ID] [--workspace_name WORKSPACE_NAME] --file_id FILE_ID [--file_paths FILE_PATHS [FILE_PATHS ...]] [--all [{true,false}]] [--json-output [{pretty,default}]]
                [--yaml-output [{true,false}]]

options:
  -h, --help            show this help message and exit
  --workspace_id WORKSPACE_ID
                        Workspace ID where the Git Folder is located.
  --workspace_name WORKSPACE_NAME
                        Workspace name as an alternative to workspace_id.
  --file_id FILE_ID     File ID of the Git folder within the workspace.
  --file_paths FILE_PATHS [FILE_PATHS ...]
                        List of full file paths to discard.
  --all [{true,false}]  If set to 'true', discards changes for all files within the Git folder. (default: false)
  --json-output [{pretty,default}]
                        Specifies the format of JSON output. (default: pretty)
  --yaml-output [{true,false}]
                        Displays the information in YAML format if set to 'true'. (default: false)
```

- Example:

```bash
yeedu git discard --workspace_id=123 --file_id=456 --file_paths="/repo/file1.py,/repo/file2.js"
```

- Console output:

```bash
{
  "message": "Files discarded successfully."
}
```
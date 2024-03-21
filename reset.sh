#!/bin/bash

# set -e

source ./scripts/reset.sh
# ---------------------------------------------------------------------- #
# Define Docker Variables
# ---------------------------------------------------------------------- #
declare -a images=(
    code_py
)
declare -a volumes=(
    crawler_database_data
    crawler_dashboard_data
    crawler_dashboard_config
)
declare -a bindings=(
    client/sqlite.db
    client/data/*
    src/data/websites
    src/sqlite.db
    src/data/json
    volumes/pgadmin/
    volumes/data/
)

# ---------------------------------------------------------------------- #
# Main Function
# ---------------------------------------------------------------------- #
main(){
    # Shut down all containers
    docker compose down
    
    # End Reverse Proxy
    end_proxy
    
    # Clean up
    run folders remove_folders  ${bindings[*]}
    run volumes remove_volumes  ${volumes[*]}
    run images  remove_images   ${images[*]}
    prune_docker
}

main $@

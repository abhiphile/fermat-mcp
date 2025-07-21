#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Variables
VENV=".venv"
UV="uv"
CONFIG="mcp_config.json"


# Function to create virtual environment
create_venv() {
    echo -e "${GREEN}Creating virtual environment with uv...${NC}"
    if [ ! -d "$VENV" ]; then
        $UV venv $VENV
        . $VENV/bin/activate && $UV pip install --upgrade pip
    else
        echo -e "${YELLOW}Virtual environment already exists${NC}"
    fi
}

# Function to install dependencies
install_deps() {
    if [ ! -d "$VENV" ]; then
        create_venv
    fi
    echo -e "${GREEN}Installing dependencies...${NC}"
    . $VENV/bin/activate && \
    $UV pip install -e . && \
    $UV pip install -e ".[dev]"
}

# Function to run the server
run_server() {
    if [ ! -f "$CONFIG" ]; then
        echo -e "${YELLOW}Creating default MCP configuration file...${NC}"
        echo '{"transport": "stdio", "log_level": "info"}' > $CONFIG
        echo -e "${GREEN}Created $CONFIG with default settings${NC}"
    fi
    echo -e "${GREEN}Starting MCP server...${NC}"
    . $VENV/bin/activate && \
    $UV run server.py
}

# Run the server
create_venv
install_deps
run_server

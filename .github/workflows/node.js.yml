name: Node.js CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:

    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [16.x]

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Use Node.js ${{ matrix.node-version }} in 'client' directory
      run: |
        cd client
        export NODE_OPTIONS=--openssl-legacy-provider
        npm install
        npm run build --if-present
        npm test
      shell: bash

    - name: Use Node.js ${{ matrix.node-version }} in 'server' directory
      run: |
        cd server
        npm install
        npm run build --if-present
        npm test
      shell: bash

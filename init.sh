#!/bin/sh

upgradevenv ()
{
    source venv/bin/activate &&
    pip install --upgrade -r requirements.txt  &&
    deactivate
}

[ -d venv ] && upgradevenv || virtualenv venv && upgradevenv

exit 0

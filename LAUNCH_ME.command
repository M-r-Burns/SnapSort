#!/bin/bash
cd "$(dirname "$0")"

echo "------------------------------------------------"
echo "   STARTING PHOTO SORTER (Port 5001)..."
echo "   Installing Dependencies..."
echo "------------------------------------------------"

# 1. Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "First time setup... Creating virtual environment..."
    python3 -m venv venv
fi

# 2. Activate it
source venv/bin/activate

# 3. Install Flask, Image Converters, and TKinter helper
# We add 'tk' here just in case, though usually it's a system level install.
pip install flask pillow pillow-heif > /dev/null 2>&1

# 4. Run the App
python3 app.py
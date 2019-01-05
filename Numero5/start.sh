
if [ -z "$1" ]; then
    echo "usage: ./start.sh [substring]"
    exit 1
fi

./filtre.erl $1

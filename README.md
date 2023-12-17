# stock-viz-backend-flask
python flask backend for a stock viz app


#running db from commmand line
cat stock_viz.sql | docker exec -i pg_container psql


# to do:
# update types for table (done)
# create apis
# global search for users and tweets and then delete
# create integrations with alembic
# test api with insomnia (start with post api)
# add html pages for displaying a few stocks and price on a table
# verify post is working locally on table
# verify delete is working on html table
# create a docker image
# run from the cloud
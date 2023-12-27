# stock-viz-backend-flask
python flask backend for a stock viz app


#running db from commmand line
cat stock_viz.sql | docker exec -i pg_container psql


# to do:
# update types for table (done)
# create apis (done)
# global search for users and tweets and then delete (done)
# create integrations with alembic []
# test api with insomnia (start with post api) (done)
# add html pages for displaying a few stocks and price on a table
# verify post is working locally on table (done)
# verify delete is working on html table []
# create a docker image for just flask(done)
# run flask app using docker image(done)
# upgrade to using .env for db information (done)
# create a docker compose for database , network and webapp borrow example from workshop (done)
# re-run app with docker compose (done)
# deploy docker app to the cloud - google cloud []
# run cloud version of app from my personal browser []

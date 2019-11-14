# Simple Hello World Flask App for deployment on Cloudfoundry


Can be deployed on GOVUK PaaS with:

```
cf push --no-start
cf set-env digitalmarketplace-supplier-data-prototype BASIC_AUTH_USERNAME <SOME_USERNAME>
cf set-env digitalmarketplace-supplier-data-prototype BASIC_AUTH_PASSWORD <SOME_PASSWORD>
cf start simple-flask-fe
```

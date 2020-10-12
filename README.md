# Refactoring a monolithic application to microservices
This repository contains the code used in the tutorials [Inter-service communication in a microservices setup](https://cloud.google.com/solutions/inter-services-communication-in-microservices) and [Distributed tracing in a microservices application](https://cloud.google.com/solutions/distributed-tracing-in-microservices).

These tutorials take example of a dummy ecommerce application and walks through the steps of converting the monolithic application to microservices. The tutorial series demonstrates microservices development using [Strangler Pattern](https://martinfowler.com/bliki/StranglerFigApplication.html) for checkout and payment flows in the example ecommerce application. Other details covered include distributed transactions spanning across microservices boundaries, compensations implementation using [Sagas](https://microservices.io/patterns/data/saga.html), isolating microservices using gRPC and OpenCensus/Stackdriver based distributed tracing for a polyglot application running different protocols (HTTP and gRPC).

## Disclaimer
This is not an officially supported Google product.


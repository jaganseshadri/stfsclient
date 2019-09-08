# Simple TensorFlow Serving Client

A simple, consolidated, extensible [gRPC](https://grpc.io/)-based client implementation for querying a hosted `tensorflow_model_server`.

**What it does do?**

It simplifies working with [protocol buffers](https://developers.google.com/protocol-buffers/) and provides custom functions for working with `protobuf` APIs (i.e. messages and services) inside [Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving) , all without leaving the comfort of python. 

Implements gRPC client stubs for `GetModelMetadata`, `GetModelStatus`, `HandleReloadConfig` and `Predict` APIs. 

**What it doesn't do?**

It doesn't completely abstract away working with protocol buffers. The internal protocol buffer can still be accessed and manipulated using methods specific to protocol buffers. This is preferred when working with gRPC clients that expect raw protocol buffers.

For a more detailed reference, [click here](/docs/DESIGN.md).

## Installation

### Client

```bash
pip install git+https://github.com/jagans94/stfsclient.git
```

### `tensorflow_model_server` 

#### Debian/Ubuntu

**Note:** Run as `sudo`

```bash
echo "deb http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | tee /etc/apt/sources.list.d/tensorflow-serving.list && \
curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add -
apt update
apt-get install tensorflow-model-server
```

#### Docker

```bash
TBD
```

## Tutorial

Refer here for the most up-to-date [tutorial.](./extras/tutorial/tutorial.ipynb)

## Benchmarks

 ![](./docs/latency_profile_mnist.png)

gRPC predict requests have a lot smaller latency profile (approx. 6 times faster) when compared with REST based requests on MNIST data set! :)

**Note:** Code for bench marking can be found at  [extras/benchmarks.](./extras/benchmarks)

## To Do

The basic implementation is almost complete. However, there are some add-ons that would be well worth expanding on. Here are some:

### General

- [ ] Documentation

### Message

- [ ] Reduce replicated `property` logic by defining custom [descriptors](https://docs.python.org/3/howto/descriptor.html).
- [ ] Implement `Classify`,  `Regress` and `MultiInference` APIs.
- [ ] Write test script for expected behaviours for each wrapper class as well as a generic test suite covering the base class implementation.
- [ ] Add parser for reading `signature_def` from  `GetModelMetadataResponse`.
- [ ] Extend `tensor_proto` conversion utilities to fully support all operations supported natively in TensorFlow.

### gRPC

- [ ] Add examples for asynchronous requests.
- [ ] Create a gRPC service for downloading a model from a blob store on client request. 
- [ ] Create  gRPC service for querying latest versions available from a blob store and making them available automatically, based on policy, etc.
- [ ] Support authentication (gRPC already supports authentication. However, the wrapper around the gRPC client services uses `insecure_channel` for communication. Ideally, I'd like to extend authentication support for  both client, i.e. this library and server, i.e. hosted  `tensorflow_model_server` using the many already in-built authentication mechanisms as well as custom plugins)
- [ ] Add more bench-marking tests for gRPC vs REST API endpoints.

## Contributions:

Want to add a feature that's not in here or implement the ones above. Raise an **Issue** or better yet **PR**. ;)

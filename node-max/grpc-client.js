"use strict";

const config = require("./config.json");
const grpc = require("grpc");
const proto = grpc.load(`${__dirname}/../scheme/main.proto`);

const client = new proto.SearchService(
  `localhost:${config.port}`,
  grpc.credentials.createInsecure()
);

module.exports = {
  client,
};

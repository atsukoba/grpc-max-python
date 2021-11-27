const grpc = require("./grpc-client");
const path = require("path");
const Max = require("max-api");

// This will be printed directly to the Max console
Max.post(`Loaded the ${path.basename(__filename)} script`);

// Use the 'addHandler' function to register a function for a particular message
Max.addHandler("bang", () => {
  Max.post("Who you think you bangin'?");
});

// Use the 'outlet' function to send messages out of node.script's outlet
Max.addHandler("echo", (msg) => {
  Max.outlet(msg);
});

Max.addHandler("search", (msg) => {
  grpc.client.search(
    {
      requester: msg,
    },
    (err, res) => {
      if (err) {
        Max.post("Error!");
        return console.error(err);
      }
      Max.post(res);
    }
  );
});

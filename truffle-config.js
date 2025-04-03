module.exports = {
  networks: {
    development: {
      host: "192.168.1.26",
      //host: "192.168.17.10",
      port: 7545,
      network_id: "*",
    },
  },
  compilers: {
    solc: {
      version: "0.8.0",  // Usa la stessa versione del contratto
    },
  },
};

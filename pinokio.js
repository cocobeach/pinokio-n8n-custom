const { app } = require('electron');
const path = require('path');

module.exports = {
  onStart: () => {
    console.log('n8n starting...');
  },
  onStop: () => {
    console.log('n8n stopped.');
  }
};

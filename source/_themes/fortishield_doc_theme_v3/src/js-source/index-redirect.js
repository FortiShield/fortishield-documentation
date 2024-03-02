let url;
switch (document.location.protocol) {
  case 'http':
  case 'https':
    url = document.location.protocol + '//' + document.location.host;
    break;
  default:
    url = 'https://fortishield.github.io/documentation';
}

document.location = url + '/' + DOCUMENTATION_OPTIONS.VERSION + '/getting-started/index.html';

@Resources = new Meteor.Collection 'resources'

Resources.initEasySearch 'meta',
  limit: 1000

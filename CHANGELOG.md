# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [2.2] - 2019-01-29

## Fixed

- Default owner now assigned automatically to the current logged in user / field hidden
- Path buggy schedule checking timezone utilization
- Schedules may now have N open times

## Added

- Admin action to bulk apply schedules to facilities
- Changed default image
- Alert model refactored to support URLs, subjects, and bodies
- Add front royal location as an option

## Removed

- Mason Korea support dropped
- Deprecated previous Alert model
- Drop label support
- Drop Sodoxo classifier
- Drop schedule promotion
- Drop schedule deletion

## [2.1.1] - 2017-01-13

## Fixed

- phone_number now is actually serialized

## [2.1.0] - 2017-12-29

### Added

- Django 2.0
- Facility tagging overhaul (tags, labels, and classifiers)
- Facilites can have phone numbers
- Special Schedules can be promoted to Main Schedule status on a provided datetime
- "Note" field added to Facilites
- Facilities can have associated logos
- "Friendly" building names
- Option to allow special schedules to not expire
- Docker Swarm integration

### Changed

- The map in the admin for Location now has a default (x,y) position over GMU FFX rather than the middle of the ocean
- Special Schedules can start at a specific time on a date

[2.1.0]: https://git.gmu.edu/srct/whats-open/compare/2.0...2.1
[2.1.1]: https://git.gmu.edu/srct/whats-open/compare/2.1...2.1.1

# Requirements for a simple filesystem
A filesystem should allow to:

1. Create a file
1. Open and close file
1. Write to file
1. Read from file
1. Seek in file

Other things outside the scope: directories, permissions, concurrency and locking, renaming, atomic operations, consistency/checksums, etc.

## distributed filesystem

A distributed filesystem should do all of the above plus:
1. Be available from multiple computers
1. Data redundancy
1. Error resilient, fail-over

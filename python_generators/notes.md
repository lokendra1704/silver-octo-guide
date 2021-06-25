# Generators

<p>The function with yield is called a generator function
</p>
<p>Generator function when called, always returns a generator object.</pr>
<p>A Generator Function has an intial entry point which is just like a regular function. A yield Statements defines an exit point and simultaneously a re-entry point.
</p>
<p>Functions which have entry and exit points are called as Coroutines</p>

## <b>Iterator Protocol</b>

Any object in Python can be a iterator. It just needs to define proper `__iter__` and `__next__` methods.

##### Note: Bottleneck Alert! Don't use file.readlines() in a program if you want to make it scalable or in coroutines because it takes all the data of text file and splits by "\n". Better option would be next(file_handle) or `for line in file:`

## <b>Scalabale Composability</b>
<p>When you design componenets in your applications that are themselves scalable, that can handle increasing magnitude of data gracefully and scalably and, They can be composed together to create other scalable components to create internal data processing pieplines.</p>

## <b>Record Mapping</b>
<p> You can think of generator's functions as mapping one stream of records to another stream
With parse_log_records, one input record maps to one_output record:

<ol>
<li>Input Record: one line</li>
<li>Output Record: one dict</li>
</ol>

<p>What happens when the mapping isn't one-to-one?</p>
<ul>
<li>Several input records are consumed to produce one output record. (Solution: house_records.py)</li>
<li>One input record create several output records</li>
</ul>
from context import sample

print(sample)
print(sample.hmm)
print(sample.core)
print(sample.core.hmm)
print(sample.core.get_hmm)
print(sample.core.helpers)
print(sample.core.helpers.get_answer)

print(sample.core.helpers.get_answer())
print(sample.core.get_hmm())
sample.core.hmm()
sample.hmm()

print(sample.thingtotext)
print(sample.side.thingtotext)
thing = 123
print(type(thing), type(sample.thingtotext(thing)))

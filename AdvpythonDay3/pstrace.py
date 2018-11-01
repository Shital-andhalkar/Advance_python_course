from psemp import main
from trace import Trace

trace_instance=Trace()
trace_instance.run('main()')

r=trace_instance.results()
r.write_results(coverdir='covers')
Tps：在实际测试中表现为：

一个系统吞吐量通常由QPS（TPS）、并发数两个因素决定，每套系统这两个值都有一个相对极限值，在应用场景访问压力下，只要某一项达 到系统最高值，系统的吞吐量就上不去了，如果压力继续增大，系统的吞吐量反而会下降，原因是系统超负荷工作，上下文切换、内存等等其它消耗导致系统性能下降。
实际表现为tps即先上升后下降，我们需要找到性能拐点。并得到限制瓶颈






Requests per second: 91.50 [#/sec] (mean) //平均(mean)每秒完成的请求数：QPS，这是一个平均值，等于Complete requests/Time taken for tests=100/1.093=91.50







ab -n 100 -c 100 http://192.168.6.96/v2/users//test

ab -n 100 -c 100 http://192.168.6.95/

ab -n 100 -c 100 http://192.168.6.92/userportal/api/list_vms








ab -n 100 -c 100 http://192.168.6.92/v2/events/

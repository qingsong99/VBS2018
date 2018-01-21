# Video Browser Showdown - 2018

This is the VBS Search system based on locally regional object proposal.

If you use this is your system, please cite to this paper:

+ Title: *Video Search Based On Semantic Extraction And Locally Regional Object Proposal*.

+ Author: ***Thanh-Dat Truong**, Vinh-Tiep Nguyen, Minh-Triet Tran, Van-Tien Do, Trang-Vinh Trieu, Thanh Duc Ngo and Duy-Dinh Le*

## Requirements:

+ python 2.7

+ Library: httplib, BaseHTTPServer, numpy, pickle, json

+ You need to download features which were extracted. Link download will be update after.

## Useage:

First of all, we need to create database for Server. You need to execute run.sh in CreateDatabase folder.

```bash
cd CreateDatabase
./run.s
```

After that, you need to run server. Server will run on local host at 8088 port.

```bash
cd ../Server
python server.py
```

If you want to request to server, you have to have a input files with json format named Query.json (it has to be in Server folder). The format of input is a list of object and its position.

```
<object 1 name>, <row number>, <column number>
```

To request, you run Client/client.py.

```bash
python Client/client.py
```

The result is in text file named result.txt. The format of result is:

```
TRECVID2016_<video number>.<shot id>..txt
```

## License

The source code uses for academic only. Please email me if you want to use for another purpose.

## Author

Thanh-Dat Truong

University of Science, Vietnam National University

Multimedia Communications Laboratory, University of Information Technology, Vietnam National University

Email: dattt@uit.edu.vn
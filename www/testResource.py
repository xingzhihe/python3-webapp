from com.phoenix.resource import Resource, ResourceFactory, ResourceService

srv = ResourceService()

#srv.add("sys:[aa,bb,cc]")
#srv.add("user:[hxz,yjm,hp]")
#srv.add("base_res:[label,description]")
#srv.add("base_res#int:[label:整数,description:整数]")
#srv.add("base_res#string:[label:文本,description:字符串]")

#srv.add("var:[base_res#type]")
#srv.add("var#aa:[type:base_res#int]")
#srv.add("var#bb:[type:base_res#string]")

#srv.add("order:[var#id:[type:base_res#int],var#title:[type:base_res#string]]")
#srv.add("order#1:[id:1,title:哈密瓜]")
#srv.add("order#2:[id:int#2,title:string#猕猴桃]")

resource = srv.rootResource
#print(resource)

print(resource.name + ":")
for item in resource.items:
    print("\t%s" % item)
    

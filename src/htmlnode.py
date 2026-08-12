class HTMLNode:
    def __init__(self,tag:str=None,value:str=None,children:list=None,props:dict[str,str]=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self)->str:
        output = ""
        if self.props==None or len(self.props)==0:
            return output
        for key,value in self.props.items():
            output+= f' {key}="{value}"'
        return output

    def __repr__(self)->str:
        return f"HTMLNode(self,{self.tag},{self.value},{self.children},{self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag:str|None,value:str,props:dict[str,str]=None):
        super().__init__(tag,value,None,props)

    def to_html(self)->str:
        if self.value==None:
            raise ValueError("Leaf node has no value, but it must.")
        if self.tag==None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self)->str:
        return f"LeafNode(self,{self.tag},{self.value},{self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag:str,children:list,props:dict[str,str]=None):
        super().__init__(tag,None,children,props)

    def to_html(self)->str:
        if self.tag==None:
            raise ValueError("tag has to be set")
        if self.children==None:
            raise ValueError("children has to be set")
        children_string=""
        for i in range(len(self.children)):
            children_string+=self.children[i].to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"

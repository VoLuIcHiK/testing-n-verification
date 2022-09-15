from PaginationHelper import PaginationHelper

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
print(helper.page_count()) # should == 2
print(helper.item_count()) # should == 6
print(helper.page_item_count(0))  # should == 4
print(helper.page_item_count(1)) # last page - should == 2
print(helper.page_item_count(2)) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
print(helper.page_index(5)) # should == 1 (zero based index)
print(helper.page_index(2)) # should == 0
print(helper.page_index(20)) # should == -1
print(helper.page_index(-10)) # should == -1 because negative indexes are invalid

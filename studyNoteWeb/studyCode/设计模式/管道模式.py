# 定义数据处理操作的接口
class DataProcessor:
    def process(self, data):
        pass

# 具体的筛选操作类
class FilterProcessor(DataProcessor):
    def process(self, data):
        # 进行筛选操作
        filtered_data = [item for item in data if item > 0]
        return filtered_data

# 具体的删除操作类
class DeleteProcessor(DataProcessor):
    def process(self, data):
        # 进行删除操作
        cleaned_data = [item for item in data if item % 2 == 0]
        return cleaned_data

# 管道类
class Pipeline:
    def __init__(self, processors):
        self.processors = processors

    def process_data(self, data):
        for processor in self.processors:
            data = processor.process(data)
        return data

# 使用管道模式处理数据
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter_processor = FilterProcessor()
delete_processor = DeleteProcessor()

pipeline = Pipeline([filter_processor, delete_processor])

result = pipeline.process_data(data)
print(result)  # 输出: [2, 4, 6, 8, 10]

# 优点：可拓展性、可维护性、灵活性
# 缺点：
# 增加了复杂性：使用管道模式会引入额外的复杂性。需要定义和管理多个处理器以及它们之间的关系和通信。这可能增加代码的复杂性和理解难度。
# 性能开销：管道模式可能会引入额外的性能开销。因为每个处理器都需要将数据传递给下一个处理器，可能需要进行频繁的数据传输和拷贝操作，导致性能损失。


# 考虑用管道模式需要多方考虑，特别是增加复杂性这一块
# 如果某个处理器的输出需要依赖前面多个处理器的状态，就不太适合使用简单的管道模式。
